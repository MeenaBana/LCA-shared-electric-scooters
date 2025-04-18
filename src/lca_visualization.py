"""
Visualization of LCA results for shared electric scooters.

This script creates visualizations of the lifecycle assessment data
for shared electric scooters, based on the findings from the LCA report.
"""

import os
import csv
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib.patches import FancyArrowPatch


def get_project_root():
    """Get the path to the project root directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(current_dir)

def ensure_dir(directory):
    """Ensure directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_data_to_csv(data, filename):
    """Save data to a CSV file in the specified directory."""
    data_dir = os.path.join(get_project_root(), "data")
    ensure_dir(data_dir)
    filepath = os.path.join(data_dir, filename)
    
    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data.keys())
        csvwriter.writerows(zip(*data.values()))
    
    print(f"Data saved to {filepath}")


def load_data_from_csv(filename):
    """Load data from a CSV file in the specified directory."""
    data_dir = os.path.join(get_project_root(), "data")
    filepath = os.path.join(data_dir, filename)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    data = {}
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)
        for h in headers:
            data[h] = []
        
        for row in csvreader:
            for i, value in enumerate(row):
                try:
                    data[headers[i]].append(float(value))
                except ValueError:
                    data[headers[i]].append(value)
    
    return data


def create_emissions_comparison_chart():
    """
    Create a comparison chart of emissions from different transport modes.
    Data from emissions comparison section of the report.
    """
    transport_modes = ['E-Scooter', 'Bus', 'Personal Car']
    emissions = [29.5, 51, 257]  # g CO2-eq/passenger-km
    
    percent_reduction = [(1 - (e / emissions[2])) * 100 for e in emissions]
    plt.figure(figsize=(12, 8))
    
    ax1 = plt.subplot(121)
    bars = ax1.bar(transport_modes, emissions, color=sns.color_palette("viridis", len(transport_modes)))
    ax1.set_ylabel('g CO2-eq/passenger-km', fontsize=12)
    ax1.set_title('Emissions by Transport Mode', fontsize=14)
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{height}', ha='center', va='bottom')
   
    ax2 = plt.subplot(122)
    bars = ax2.bar(transport_modes, percent_reduction, color=sns.color_palette("viridis", len(transport_modes)))
    ax2.set_ylabel('% Reduction vs. Personal Car', fontsize=12)
    ax2.set_title('Emissions Reduction vs. Car', fontsize=14)
    ax2.set_ylim(0, 100)
   
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{height:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
   
    results_dir = os.path.join(get_project_root(), "results")
    ensure_dir(results_dir)
    plt.savefig(os.path.join(results_dir, 'emissions_comparison.png'), dpi=300, bbox_inches='tight')
   
    data = {
        'Transport Mode': transport_modes,
        'Emissions (g CO2-eq/passenger-km)': emissions,
        'Reduction vs Car (%)': percent_reduction
    }
    save_data_to_csv(data, 'emissions_comparison.csv')
    
    return plt.gcf()


def create_component_emissions_chart():
    """
    Create a chart showing emissions contributions from different e-scooter components.
    """
    components = ['Battery', 'Transport', 'Set of Breaks', 'Motor', 
                  'Glider', 'Handlebar', 'Wheels', 'Controller']
    emissions = [54.7051754, 21.0922214, 5.69716261, 6.61217455,
                 5.25322362, 4.63982784, 15.0252457, 89.2183668]
    
    total = sum(emissions)
    percentages = [e / total * 100 for e in emissions]
    
    sorted_indices = np.argsort(emissions)[::-1]  # Descending order
    sorted_components = [components[i] for i in sorted_indices]
    sorted_emissions = [emissions[i] for i in sorted_indices]
    sorted_percentages = [percentages[i] for i in sorted_indices]
  
    plt.figure(figsize=(14, 10))
   
    ax1 = plt.subplot(121)
    bars = ax1.barh(sorted_components, sorted_emissions, color=sns.color_palette("viridis", len(components)))
    ax1.set_xlabel('kg CO2-eq', fontsize=12)
    ax1.set_title('CO2 Emissions by Component', fontsize=14)
   
    for bar in bars:
        width = bar.get_width()
        ax1.text(width + 2, bar.get_y() + bar.get_height()/2.,
                f'{width:.1f}', ha='left', va='center')
 
    ax2 = plt.subplot(122)
    wedges, texts, autotexts = ax2.pie(sorted_emissions, 
                                     labels=sorted_components,
                                     autopct='%1.1f%%',
                                     startangle=90,
                                     colors=sns.color_palette("viridis", len(components)))
    
    plt.setp(autotexts, size=9, weight="bold")
    ax2.set_title('Component Contribution to Total Emissions', fontsize=14)
    
    plt.tight_layout()
    
    results_dir = os.path.join(get_project_root(), "results")
    ensure_dir(results_dir)
    plt.savefig(os.path.join(results_dir, 'component_emissions.png'), dpi=300, bbox_inches='tight')
   
    data = {
        'Component': components,
        'Emissions (kg CO2-eq)': emissions,
        'Percentage (%)': percentages
    }
    save_data_to_csv(data, 'component_emissions.csv')
    
    return plt.gcf()


def create_lifecycle_emissions_chart():
    """
    Create a chart showing emissions across the lifecycle phases.
    """
   
    phases = ['Manufacturing', 'Transport', 'End-of-Life']
    percentages = [87.8, 11.15, 1.05]  # Percentages reported in the document
 
    total_emissions = 202.243398  # Total from report
    absolute_values = [p * total_emissions / 100 for p in percentages]
    
    plt.figure(figsize=(12, 8))
   
    ax1 = plt.subplot(121)
    bars = ax1.bar(phases, absolute_values, color=sns.color_palette("viridis", len(phases)))
    ax1.set_ylabel('kg CO2-eq', fontsize=12)
    ax1.set_title('Emissions by Lifecycle Phase', fontsize=14)
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{height:.1f}', ha='center', va='bottom')
  
    ax2 = plt.subplot(122)
    wedges, texts, autotexts = ax2.pie(percentages, 
                                     labels=phases,
                                     autopct='%1.1f%%',
                                     startangle=90,
                                     colors=sns.color_palette("viridis", len(phases)))
    
    plt.setp(autotexts, size=10, weight="bold")
    ax2.set_title('Percentage Contribution by Lifecycle Phase', fontsize=14)
    
    plt.tight_layout()
   
    results_dir = os.path.join(get_project_root(), "results")
    ensure_dir(results_dir)
    plt.savefig(os.path.join(results_dir, 'lifecycle_emissions.png'), dpi=300, bbox_inches='tight')
   
    data = {
        'Lifecycle Phase': phases,
        'Emissions (kg CO2-eq)': absolute_values,
        'Percentage (%)': percentages
    }
    save_data_to_csv(data, 'lifecycle_emissions.csv')
    
    return plt.gcf()


def create_impact_categories_chart():
    """
    Create a chart showing different environmental impact categories.
    """
    categories = ['Global warming', 'Terrestrial acidification', 'Water consumption',
                  'Mineral resource scarcity', 'Land use', 'Marine ecotoxicity']
    
    values = [186.5430854, 2.085688716, 5.58308347, 
              21.07493509, 12.40058654, 204870.4829]
    
    units = ['kg CO2 eq', 'kg SO2 eq', 'm3', 
             'kg Cu eq', 'm2yr crop eq', 'kg 1,4-DCB']
  
    labels = [f"{cat}\n({unit})" for cat, unit in zip(categories, units)]
    
    # Normalize values for comparison (as they have different units)
    max_values = [200, 3, 10, 25, 15, 250000]  # Approximate max scale for each category
    normalized = [val / max_val * 100 for val, max_val in zip(values, max_values)]
    
    plt.figure(figsize=(14, 8))
    
    
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # Close the loop
    
    normalized_values = normalized + [normalized[0]]
   
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, normalized_values, 'o-', linewidth=2)
    ax.fill(angles, normalized_values, alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    ax.set_rlabel_position(0)
    plt.yticks([20, 40, 60, 80, 100], ['20%', '40%', '60%', '80%', '100%'], color='grey', size=8)
    plt.ylim(0, 100)
    
    plt.title('Environmental Impact Categories (Normalized)', fontsize=16)

    results_dir = os.path.join(get_project_root(), "results")
    ensure_dir(results_dir)
    plt.savefig(os.path.join(results_dir, 'impact_categories.png'), dpi=300, bbox_inches='tight')

    data = {
        'Impact Category': categories,
        'Value': values,
        'Unit': units,
        'Normalized (%)': normalized
    }
    save_data_to_csv(data, 'impact_categories.csv')
    
    return plt.gcf()


def create_lifespan_sensitivity_chart():
    """
    Create a chart showing how lifespan affects emissions.
    """
    lifespans = ['18 months', '24 months (base)']
    emissions = [39.27, 29.5]  # g CO2-eq/passenger-km
    
    percent_change = (emissions[0] - emissions[1]) / emissions[1] * 100
 
    plt.figure(figsize=(10, 6), dpi=300)
   
    bars = plt.bar(lifespans, emissions, color=sns.color_palette("viridis", len(lifespans)))
    plt.ylabel('g CO2-eq/passenger-km', fontsize=12)
    plt.title(f'Impact of Scooter Lifespan on Emissions\n({percent_change:.1f}% increase when reducing lifespan from 24 to 18 months)', fontsize=14)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height}', ha='center', va='bottom')
    
    results_dir = os.path.join(get_project_root(), "results")
    ensure_dir(results_dir)
    plt.savefig(os.path.join(results_dir, 'lifespan_sensitivity.png'), dpi=300, bbox_inches='tight')
    
    data = {
        'Lifespan': lifespans,
        'Emissions (g CO2-eq/passenger-km)': emissions
    }
    save_data_to_csv(data, 'lifespan_sensitivity.csv')
    
    return plt.gcf()


def create_circular_vs_linear_chart():
    """Create a comparison of linear vs circular economy models for e-scooters."""
    plt.close('all')
    plt.figure(figsize=(12, 8), dpi=300)
    
    colors = {
        'extract': '#FF6B6B',  # Red
        'produce': '#4ECDC4',  # Teal
        'distribute': '#FFD166',  # Yellow
        'use': '#06D6A0',  # Green
        'dispose': '#073B4C',  # Dark Blue
        'collect': '#118AB2',  # Blue
        'recycle': '#8338EC',  # Purple
        'reuse': '#3A86FF',  # Light Blue
        'repair': '#FB5607',  # Orange
    }
    
    # LINEAR ECONOMY DIAGRAM (LEFT)
    ax1 = plt.subplot(121)
    ax1.set_title('Linear Economy Model for E-Scooters', fontsize=16, pad=20)
    ax1.axis('equal')
    ax1.axis('off')
    
    steps = ['Raw Material\nExtraction', 'Manufacturing', 'Distribution', 'Use', 'Disposal']
    colors_linear = [colors['extract'], colors['produce'], colors['distribute'], colors['use'], colors['dispose']]
    positions = np.linspace(0, 4, 5)

    for i, (step, color) in enumerate(zip(steps, colors_linear)):
        rect = mpatches.Rectangle((i-0.4, 0.3), 0.8, 0.4, 
                                facecolor=color, alpha=0.8, edgecolor='black')
        ax1.add_patch(rect)
        ax1.text(i, 0.5, step, ha='center', va='center', fontsize=10, fontweight='bold')

    for i in range(len(steps)-1):
        ax1.annotate('', xy=(i+0.5, 0.5), xytext=(i+1-0.5, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    ax1.text(2, -0.4, 'Key Findings from LCA:\n• Manufacturing: 87.8% of emissions\n• Lifespan: 2 years (base scenario)\n• Emissions: 29.5 g CO₂-eq/passenger-km\n• Battery emissions: 30.2% of manufacturing', 
             ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.5'), fontsize=10)
    
    # CIRCULAR ECONOMY DIAGRAM (RIGHT)
    ax2 = plt.subplot(122)
    ax2.set_title('Circular Economy Model for E-Scooters', fontsize=16, pad=20)
    ax2.axis('equal')
    ax2.axis('off')

    n_points = 6
    radius = 1.2
    angles = np.linspace(0, 2*np.pi, n_points, endpoint=False)

    circular_steps = [
        'Sustainable\nMaterial Sourcing',
        'Modular\nManufacturing',
        'Extended\nUse Phase',
        'Maintenance\n& Repair',
        'Refurbishment',
        'Material\nRecycling'
    ]
    
    circular_colors = [
        colors['extract'], 
        colors['produce'], 
        colors['use'], 
        colors['repair'],
        colors['reuse'],
        colors['recycle']
    ]

    box_width = 0.5
    box_height = 0.3
    xs = radius * np.cos(angles)
    ys = radius * np.sin(angles)
    
    for i, (step, color, x, y, angle) in enumerate(zip(circular_steps, circular_colors, xs, ys, angles)):
        rect = mpatches.Rectangle((x-box_width/2, y-box_height/2), box_width, box_height, 
                                facecolor=color, alpha=0.8, edgecolor='black')
        ax2.add_patch(rect)
        ax2.text(x, y, step, ha='center', va='center', fontsize=9, fontweight='bold')
    
    for i in range(n_points):
        start = (xs[i], ys[i])
        end = (xs[(i+1)%n_points], ys[(i+1)%n_points])
        
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        dist = np.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
        
        # Normalize the vector perpendicular to the chord
        if dist > 0:
            norm_x = -(end[1] - start[1]) / dist
            norm_y = (end[0] - start[0]) / dist
          
            control_x = mid_x + norm_x * radius * 0.3
            control_y = mid_y + norm_y * radius * 0.3
           
            path = mpatches.Path([(start[0], start[1]), 
                                 (control_x, control_y), 
                                 (end[0], end[1])], 
                                [1, 2, 2])
            
            arrow = FancyArrowPatch(path=path, facecolor='none', edgecolor='black', lw=1.5, arrowstyle='->')
            ax2.add_patch(arrow)
    
    
    center_circle = plt.Circle((0, 0), radius=0.4, facecolor='white', edgecolor='black', alpha=0.9)
    ax2.add_patch(center_circle)
    ax2.text(0, 0, "Reduced\nEnvironmental\nImpact", ha='center', va='center', fontsize=10, fontweight='bold')
   
    ax2.text(0, -1.8, 'Potential Improvements:\n• Extend lifespan to 4+ years (−50% emissions)\n• Efficient material recovery (90%+)\n• Alternative transport routes (−71.7% transport emissions)\n• Improved collection strategies (−27.2% collection emissions)', 
             ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.5'), fontsize=10)
    
    plt.suptitle('Linear vs. Circular Economy for Shared Electric Scooters', fontsize=18, y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    results_dir = os.path.join(get_project_root(), "results")
    ensure_dir(results_dir)
    plt.savefig(os.path.join(results_dir, 'circular_vs_linear.png'), dpi=300, bbox_inches='tight')
   
    return plt.gcf()


def main():
    """Main function to generate all visualizations."""
    # Set style
    plt.style.use('ggplot')
    sns.set_palette("viridis")
 
    create_emissions_comparison_chart()
    create_component_emissions_chart()
    create_lifecycle_emissions_chart()
    create_impact_categories_chart()
    create_lifespan_sensitivity_chart()
    create_circular_vs_linear_chart()
    
    print("All visualizations created successfully!")
    print(f"Results saved to: {os.path.join(get_project_root(), 'results')}")
    print(f"Data saved to: {os.path.join(get_project_root(), 'data')}")


if __name__ == "__main__":
    main()