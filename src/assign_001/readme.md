# 🐼 Pandas assignment : 

## 📙 Description
A Data Engineer extracted some data for you before erasing it from the database. Unfortunately, an error occurred during the process, from the 3rd row the values were mixed up and no longer belong to the correct columns. As a Data Scientist, we need you to find a way to map values to the correct columns they should belong to.

## 📖 Instructions
You have to implement your solution proposal in the file `script.py`. Remove all TODO comments and lines in the code/docstrings and replace them with your own code/docstrings.

Some steps :
- Keep & respect the global structure of the file;
- Write documentation and docstrings at the dedicated space;
- Write your code at the dedicated space;
- Clean and comment your code as much as you can to make it look clear and pro.

<!-- ## 💡 Hints 💡
Some hints to help you in your adventure :
- ;
- ; -->

## 👩‍🏫 Examples
Below is a head of the dataframe you have.

|    | email                       | address                        | phone                         | name                          | geo_location                   | lucky_number                   | birth_date                     |
|---:|:----------------------------|:-------------------------------|:------------------------------|:------------------------------|:-------------------------------|:-------------------------------|:-------------------------------|
|  0 | xanthapratt7715@yahoo.edu   | Ap #842-8652 Eros Rd.          | 07 18 69 75 23                | Xantha Pratt                  | -13.684769792, -0.618230272    | 36                             | 10/20/1957                     |
|  1 | avramweaver2764@hotmail.ci  | 8799 At St.                    | 08 59 41 48 82                | Avram Weaver                  | -85.7535678464, -100.224569856 | 28                             | 04/05/1981                     |
|  2 | 715-3453 A St.              | 12/31/1954                     | Larissa Everett               | 08 29 49 72 36                | larissaeverett8428@google.com  | 26.2019121152, -15.0919571456  | 72                             |
|  3 | chantaleholder9106@yahoo.sn | 04/14/1995                     | 8353 Enim St.                 | 71.7450401792, 177.6485578752 | Chantale Holder                | 49                             | 05 55 46 51 37                 |
|  4 | P.O. Box 200, 181 At, St.   | -89.8634413056, 124.8843877376 | 09 86 47 62 57                | hamishwoods4997@yahoo.sa      | 96                             | 03/15/1998                     | Hamish Woods                   |
|  5 | 77                          | 577-748 Sed Ave                | 71.4287332352, -60.3587833856 | 09 91 18 72 95                | curranmcfadden@outlook.net     | 01/17/1991                     | Curran Mcfadden                |
|  6 | 08 57 31 26 66              | -23.573850624, -126.4811677696 | Matthew Stephenson            | Ap #445-3779 Nibh Avenue      | 72                             | 12/31/1965                     | matthewstephenson@icloud.org   |
|  7 | Nissim Sawyer               | 259-342 Nulla Av.              | 01/11/1987                    | 07 38 36 97 11                | nissimsawyer@yahoo.couk        | 84                             | -86.5503683584, -63.9793779712 |
|  8 | 08/07/1962                  | Iris Doyle                     | irisdoyle4933@yahoo.com       | 10                            | 25.0994029568, -137.5596455936 | Ap #905-2620 Non Street        | 05 43 87 97 02                 |
|  9 | 01/17/1991                  | amydillard1384@icloud.edu      | 70                            | P.O. Box 946, 2271 Libero Av. | 05 23 68 60 31                 | -17.794721792, -174.4635995136 | Amy Dillard                    |

Below is the head of the dataframe you must have after your processing.

|    | email                         | address                       | phone          | name               | geo_location                   |   lucky_number | birth_date   |
|---:|:------------------------------|:------------------------------|:---------------|:-------------------|:-------------------------------|---------------:|:-------------|
|  0 | xanthapratt7715@yahoo.edu     | Ap #842-8652 Eros Rd.         | 07 18 69 75 23 | Xantha Pratt       | -13.684769792, -0.618230272    |             36 | 10/20/1957   |
|  1 | avramweaver2764@hotmail.ci    | 8799 At St.                   | 08 59 41 48 82 | Avram Weaver       | -85.7535678464, -100.224569856 |             28 | 04/05/1981   |
|  2 | larissaeverett8428@google.com | 715-3453 A St.                | 08 29 49 72 36 | Larissa Everett    | 26.2019121152, -15.0919571456  |             72 | 12/31/1954   |
|  3 | chantaleholder9106@yahoo.sn   | 8353 Enim St.                 | 05 55 46 51 37 | Chantale Holder    | 71.7450401792, 177.6485578752  |             49 | 04/14/1995   |
|  4 | hamishwoods4997@yahoo.sa      | P.O. Box 200, 181 At, St.     | 09 86 47 62 57 | Hamish Woods       | -89.8634413056, 124.8843877376 |             96 | 03/15/1998   |
|  5 | curranmcfadden@outlook.net    | 577-748 Sed Ave               | 09 91 18 72 95 | Curran Mcfadden    | 71.4287332352, -60.3587833856  |             77 | 01/17/1991   |
|  6 | matthewstephenson@icloud.org  | Ap #445-3779 Nibh Avenue      | 08 57 31 26 66 | Matthew Stephenson | -23.573850624, -126.4811677696 |             72 | 12/31/1965   |
|  7 | nissimsawyer@yahoo.couk       | 259-342 Nulla Av.             | 07 38 36 97 11 | Nissim Sawyer      | -86.5503683584, -63.9793779712 |             84 | 01/11/1987   |
|  8 | irisdoyle4933@yahoo.com       | Ap #905-2620 Non Street       | 05 43 87 97 02 | Iris Doyle         | 25.0994029568, -137.5596455936 |             10 | 08/07/1962   |
|  9 | amydillard1384@icloud.edu     | P.O. Box 946, 2271 Libero Av. | 05 23 68 60 31 | Amy Dillard        | -17.794721792, -174.4635995136 |             70 | 01/17/1991   |


Enjoy 🚀 🚀 🚀  !