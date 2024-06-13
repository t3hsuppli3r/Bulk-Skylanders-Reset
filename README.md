----------------------------------------
# Bulk Skylanders Reset Version 1.2 (SSA - SSC and Imaginators)
----------------------------------------

Now we have three variants of the scripts :

- Bulk_Skylanders_Reset.py
- Bulk_Skylanders_Imaginators_Reset.py
- Bulk_Skylanders_Imaginators_Reset_Alt_Version.py

----------------------------------------

- Bulk_Skylanders_Reset.py is for Skylander dumps from SSA to SSC.

----------------------------------------

- Bulk_Skylanders_Imaginators_Reset.py is the new script to be used for Bulk Imaginators dumps reset.
Have almost the same functionality but the wiping requirements are different for Imaginators. Read bellow.

----------------------------------------

- Bulk_Skylanders_Imaginators_Reset_Alt_Version.py will give you the same result as the "Bulk_Skylanders_Imaginators_Reset.py" from above, however the code implementation here is a bit different. You need to put the original dumps inside "input" folder and you will get the results from "output". It was written thanks to a crushing individual from Discord :)

----------------------------------------
How does it works?
----------------------------------------

Just put several Skylanders .dump files in the same directory where you've placed the "Bulk_Skylanders_Reset.py" script (or whatever variant of the script you have).

You can also place folders and subfolders with dumps, those will be also processed and overwritten.
Then open "cmd" in that same directory and type:

python Bulk_Skylanders_Reset.py

* Or whatever script variant you have, like "python Bulk_Skylanders_Imaginators_Reset.py" or another one. You can also double-click on the .py file if you have the file extension associated with Python.

----------------------------------------
What does it do?
----------------------------------------

Bulk_Skylanders_Reset.py

It preserves data on:

Sector 0
All Sector Trailers

And wipes everything else.

----------------------------------------

Bulk_Skylanders_Imaginators_Reset.py and Bulk_Skylanders_Imaginators_Reset_Alt_Version.py

It preserves data on:

Sector 0 (as the previous non-imaginators dumps)
All Sector Trailers (as the previous non-imaginators dumps)

Sector 1, Block 0 (Imaginators Signature Data)
Sector 8, Block 2 (Imaginators Signature Data)
Sector 15, Block 2 (Imaginators Signature Data)

And wipes everything else.

----------------------------------------

![00. Skylanders Hex Explained](https://raw.githubusercontent.com/t3hsuppli3r/Bulk-Skylanders-Reset/main/img/00.%20Skylanders%20Hex%20Explained.png)

![01. Skylanders Resetting SSA - SSC](https://raw.githubusercontent.com/t3hsuppli3r/Bulk-Skylanders-Reset/main/img/01.%20Skylanders%20Resetting%20SSA%20-%20SSC.png)

![02. Skylanders Resetting Imaginators](https://raw.githubusercontent.com/t3hsuppli3r/Bulk-Skylanders-Reset/main/img/02.%20Skylanders%20Resetting%20Imaginators.png)