import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import numpy as np
import PIL
from pathlib import Path

plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (16, 9)

# put your images in this folder (don't include the bad ones after #56), then run colin.py
# the csvs will be generated
img_folder = os.path.join("5 - Test1")

csv_folder = os.path.join("5 - Test1", "pydic", "result")

output_base_folder = os.path.join("output_plots")

strain_key = "strain_yy"

# the filenames must sort the same way -- don't rename them
# a better way to do this would be to look at the final number in the filename or something
img_filelist = [file for file in sorted(os.listdir(img_folder)) if file.endswith('.png')]
csv_filelist = [file for file in sorted(os.listdir(csv_folder)) if file.endswith('.csv')]

suffix_list = []

for i in range(len(img_filelist)):
    img_filename = img_filelist[i]
    csv_filename = csv_filelist[i]
    img_number_str = img_filename.split('.')[-2].split('-')[-1].strip()
    csv_number_str = csv_filename.split('.')[-2].split('-')[-1].split('_result')[0].strip()
    if img_number_str != csv_number_str:
        print("img {0} [{1}] and csv {2} [{3}] numbers didn't line up!".format(img_filename, img_number_str, csv_filename, csv_number_str))
        exit(1)
    
    suffix_list.append(img_number_str)

def plot_result(csv_path, img_path, output_folder, suffix, strain_key, show_plots=True, save_plots=True):
    if save_plots:
        Path(output_folder).mkdir(exist_ok=True)
        
        histogram_folder = os.path.join(output_folder, "histograms")
        scatterplot_folder = os.path.join(output_folder, "scatterplots")
        interpolation_nearest_folder = os.path.join(output_folder, "interpolation_nearest")
        interpolation_linear_folder = os.path.join(output_folder, "interpolation_linear")

        Path(histogram_folder).mkdir(exist_ok=True)
        Path(scatterplot_folder).mkdir(exist_ok=True)
        Path(interpolation_nearest_folder).mkdir(exist_ok=True)
        Path(interpolation_linear_folder).mkdir(exist_ok=True)


    img = PIL.Image.open(img_path, mode='r')
    df = pd.read_csv(csv_path)

    # drop rows with NaN (seems to be where markers are missed --> no markers for grid cell)
    df = df.dropna()

    # move mesh/grid from original position by displacement
    # have to set rm_rigid_body_transform=False in pydic.read_dic_file for this to work ;)
    df['curr_x'] = df["pos_x"] - df["disp_x"]
    df['curr_y'] = df["pos_y"] - df["disp_y"]

    # based on histogram and visual inspection, pick tightest range that shows most datapoints
    std = np.std(df[strain_key])
    mean = np.mean(df[strain_key].to_numpy())
    clip_std = 3
    strain_min = mean - std*clip_std
    strain_max = mean + std*clip_std

    plt.axvline(x = strain_min, color = 'red', label = 'strain_min')
    plt.axvline(x = strain_max, color = 'red', label = 'strain_max')

    # histogram is useful for throwing out "outliers"
    sns.histplot(data=df, x=strain_key)
    plt.title("[{}] {} histogram: clip (-{}std, +{}std), or ({:.6f}, {:.6f})".format(suffix, strain_key, clip_std, clip_std, strain_min, strain_max))
    if save_plots:
        plt.savefig(os.path.join(histogram_folder, "{}.png".format(suffix)))
    if show_plots:
        plt.show()
    plt.clf()
    

    # filter df
    df = df[(df[strain_key] > strain_min) & (df[strain_key] < strain_max)]

    fig = plt.figure()
    plt.imshow(img, cmap=plt.cm.binary)
    ax = sns.scatterplot(data=df, x="curr_x", y="curr_y", hue=strain_key, s=1, palette=plt.cm.rainbow)
    plt.title("[{}] {}".format(suffix, strain_key))
    if save_plots:
        plt.savefig(os.path.join(scatterplot_folder, "{}.png".format(suffix)))
    if show_plots:
        plt.show()
    plt.clf()

    # extract x and y
    x = df["curr_x"].to_numpy()
    y = df["curr_y"].to_numpy()
    # format for meshgrid
    xy = np.column_stack([x.flat, y.flat]) # Create a (N, 2) array of (x, y) pairs.
    z = df[strain_key].to_numpy()

    # Interpolate and generate heatmap:
    grid_x, grid_y = np.mgrid[x.min():x.max(), y.min():y.max()]

    # methods = ['nearest', 'linear']
    methods = ['nearest']
    for method in methods:
        grid_z = scipy.interpolate.griddata(xy,z,(grid_x, grid_y), method=method)

        fig = plt.figure()

        ax = plt.imshow(img, cmap=plt.cm.binary)
        plt.title("[{}] {} interpolation: {}".format(suffix, strain_key, method))
        # im = plt.contourf(grid_x, grid_y, grid_z, 10, cmap=plt.cm.rainbow,
        #                     vmax=strain_max, vmin=strain_min, alpha=0.5)
        im = plt.pcolormesh(grid_x, grid_y, grid_z, cmap=plt.cm.rainbow,
                            vmax=strain_max, vmin=strain_min, alpha=0.5)
        
        cb = fig.colorbar(im)
        
        if save_plots:
            if method == 'nearest':
                plt.savefig(os.path.join(interpolation_nearest_folder, "{}.png".format(suffix)))
            elif method == 'linear':
                plt.savefig(os.path.join(interpolation_linear_folder, "{}.png".format(suffix)))
        if show_plots:
            plt.show()
        plt.clf()

for strain_key in ["strain_xx", "strain_yy", "strain_xy"]:
    output_folder = os.path.join(output_base_folder, strain_key)
    for i in range(1, len(suffix_list), 1):
        img_filename = img_filelist[i]
        img_path = os.path.join(img_folder, img_filename)
        csv_filename = csv_filelist[i]
        csv_path = os.path.join(csv_folder, csv_filename)
        suffix = suffix_list[i]

        print("[{}/{}]".format(suffix, suffix_list[-1]))

        plot_result(csv_path=csv_path, img_path=img_path, output_folder=output_folder, suffix=suffix, strain_key=strain_key, show_plots=False)


# csv_path = os.path.join(csv_folder, "fc2_save_2023-02-17-152134-0050_result.csv")
# img_path = os.path.join(img_folder, 'fc2_save_2023-02-17-152134-0050.png')
# plot_result(csv_path=csv_path, img_path=img_path, output_folder=output_folder, suffix="aaa", strain_key=strain_key, show_plots=False)