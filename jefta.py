import pandas as pd
import matplotlib.pyplot as plt

# from json import loads, dumps




def methodejefta():
    df_filtered= pd.read_csv("df_filtered.csv")

    df_filtered = df_filtered.sort_values('year')


    # Calculate the minimum and maximum employment values
    # min_value = df_filtered['employment'].min()
    # max_value = df_filtered['employment'].max()

    # Create the plot
    # plt.figure(figsize=(10, 6))
    # plt.plot(df_filtered['year'], df_filtered['employment'])

    # Set the y-axis limits
    # plt.ylim([min_value, max_value])

    # Set the title and labels
    df_filtered['year'] = pd.to_datetime(df_filtered['year']).dt.year
    df_filtered['year'] = pd.to_datetime(df_filtered['year'], format='%Y')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_filtered['year'], df_filtered['employment'])

    ax.set_title('Employment over time for selected group')
    ax.set_xlabel('Year')
    ax.set_ylabel('Employment')
    n = 1  # Choose every 10th label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]


    # Show the plot
    # plt.show()


#   for i,job in bestand.iterrows():
#     if(job["JobID"]==int(jobid)):
#       pass
#     else:
#       bestand=bestand.drop(i)

#   result=bestand.to_json(orient="records")
#   parsed=loads(result)
    return fig,ax

# fig, ax = create_figure()

# plt.show()

# fig, ax = methodejefta()
# plt.show()










# def methodejefta(jobid):
#   bestand = pandas.read_csv("nyc-jobs.csv")
#   for i,job in bestand.iterrows():
#     if(job["JobID"]==int(jobid)):
#       pass
#     else:
#       bestand=bestand.drop(i)

#   result=bestand.to_json(orient="records")
#   parsed=loads(result)
#   return dumps(parsed,indent=4)




  # return "dit komt van jefta"

# jobid=87990
# bestand = pandas.read_csv("nyc-jobs.csv")
# for i,job in bestand.iterrows():
#   if(job["JobID"]==jobid):
#     print(methodejefta(87990))

# print(type(jobid))