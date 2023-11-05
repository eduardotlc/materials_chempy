TODO
====

Client
------

- Separate cli main function in smaller functions

- Check utils functions absolute_path and remove_duplicates (Might delete).

- Add spinger function

- add scopus function to the others db functions

- add db_stats, as well as any df stat

- add bar plot

Mass Spectrometry
-----------------

- Make script to plot MS2

- See the possibillity of adding peaks that have difference lower than given resolution

Documentation
-------------

- Correct not found class error, from docstrings, like pd.DataFrame and matplotlib types

- Add plots/nbs to the documentation

- Add springer function

Notebooks
---------


Data analysis
-------------

- Check if kwargs type values are correct by testing

- Create an conditional if queryied articles in a month is more than 9999, to split
  the month and than add the results.

- Check statistic function and find_matching_postions. (Might delete them)

- Probably remove read_pubmed_csv function (deprecated, use clean_csv instead)

- Remove my springer api from the code, try to use as an environment variable
