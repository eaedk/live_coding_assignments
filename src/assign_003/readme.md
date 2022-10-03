# 🐼 Pandas ft.  ➕➖✖️➗ 🔢📏 Numpy assignment : 

## 📙 Description
As a Data Scientist, we need you to process a bunch of user data to help a company. This company wants to encourage users to meet. In each country of residence, find for any user the user who is closest based on the `geo_location`, then add a column `closest_user_id` containing the id of the closest user.

**NB:** Use `Numpy` to compute the distances.

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
Below is the head of the dataframe you must have after your processing.

| user_id   | email                         | address                         | phone          | name            | residency          | region                    | city          | geo_location                    |   lucky_number | nationality        | birth_date   | closest_user_id   |
|:----------|:------------------------------|:--------------------------------|:---------------|:----------------|:-------------------|:--------------------------|:--------------|:--------------------------------|---------------:|:-------------------|:-------------|:------------------|
| M95HJR9JU | claytonwong@protonmail.sa     | 148-1022 Cursus, Rd.            | 04 08 37 18 27 | Clayton Wong    | Singapore          | West Region               | Bukit Panjang | -19.8040174592, -101.0582991872 |             81 | India              | 09/04/1947   | Y48CUX5ZL         |
| F53XVP5ST | cassandrachase@google.org     | 753-7563 Adipiscing. St.        | 03 47 15 68 73 | Cassandra Chase | Mexico             | Oaxaca                    | Oaxaca        | -51.6316346368, 54.1171785728   |             70 | France             | 08/07/1997   | A38BQT3RE         |
| L75VYW9VD | erinflynn@hotmail.edu         | P.O. Box 456, 2213 Quam Avenue  | 07 71 95 34 95 | Erin Flynn      | Chile              | Metropolitana de Santiago | Isla de Maipo | -65.9995358208, 26.3719548928   |             33 | Netherlands        | 02/09/1956   | K86CDK6SV         |
| Q87ZNU6NL | gingerbrowning2421@icloud.ca  | 9376 Arcu St.                   | 07 42 12 57 42 | Ginger Browning | Russian Federation | Kurgan Oblast             | Kurgan        | -52.08278016, 63.3369558016     |             99 | Italy              | 06/19/1966   | A57HQZ5HB         |
| I27IIM7UQ | cleopate9480@hotmail.edu      | Ap #385-5987 Gravida St.        | 01 96 11 18 87 | Cleo Pate       | Norway             | Agder                     | Grimstad      | 80.3049392128, -111.5436986368  |             63 | South Korea        | 08/04/1979   | X89USL9XW         |
| D26EGU8PE | elijahbyrd@yahoo.org          | P.O. Box 102, 8018 Cursus St.   | 08 32 87 66 13 | Elijah Byrd     | France             | Île-de-France             | Créteil       | -35.5227779072, 171.4381535232  |             32 | India              | 06/27/1964   | C46KTR9DC         |
| H35HVB4BB | calvinsanchez2765@outlook.edu | 640-5845 Phasellus St.          | 04 94 20 45 63 | Calvin Sanchez  | Brazil             | Paraíba                   | Patos         | -18.0330957824, 160.9026902016  |             33 | New Zealand        | 09/06/1975   | J11IRD1IN         |
| T36ZVH6RG | eatoncalderon3842@yahoo.ca    | P.O. Box 890, 3285 Elit, Rd.    | 03 35 65 67 56 | Eaton Calderon  | Spain              | La Rioja                  | Logroño       | -36.2797341696, 102.7425727488  |             47 | China              | 06/03/1994   | M85QQH8OG         |
| Q73KPW5FI | fatimamays728@google.gh       | P.O. Box 414, 6483 Praesent St. | 02 82 18 06 54 | Fatima Mays     | Norway             | Møre og Romsdal           | Kristiansund  | -50.6909459456, -145.7369083904 |             62 | Russian Federation | 02/18/1946   | X89USL9XW         |
| K86CDK6SV | altheasolomon5983@aol.edu     | 826-2406 Libero. Road           | 05 74 86 30 32 | Althea Solomon  | Chile              | Aisén                     | Guaitecas     | -34.2057099264, 13.9085142016   |             65 | Australia          | 02/22/1971   | L75VYW9VD         |


Enjoy 🚀 🚀 🚀  !