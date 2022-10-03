# 🐼 Pandas assignment : 

## 📙 Description
As a Data Scientist, we need you to process a bunch of user data to help a company. 

Here are the steps of the processing:

1. Some countries changed their telephone dialing. Update phone numbers of people having those countries residency, following these details :
     - Add `(99)` at the start of the phone number of the `Australia's residents`.

1. There is an issue with our mailing system, it doesn't work anymore with `aol`. Delete all the users having `aol` as mail provider.

1. We want to have some stats from our users. Below the details :
    
     - Add a column `north_american` containing `1` if the user has a nationality from `North America` (USA, Canada), otherwise `0`.

    - Add a column `china_resident` containing `1` if the user is resident in China, otherwise `0`.

    - Add a column `china_usa_cooperation` containing `1` if the user is `from USA and resident in China` or `from China and resident in USA` , otherwise `0`.

    - Add a column `day_of_birth_day` containing the day of the week of the user's birth date, encoded using 3 charaters like that : ` "Mon", "Tue", "Wed", ... `.


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

|    | email                         | address                             | phone          | name               | residency      | region              | city       | geo_location                   |   lucky_number | nationality   | birth_date   |   north_american |   china_resident |   china_usa_cooperation | day_of_birth_day   |
|---:|:------------------------------|:------------------------------------|:---------------|:-------------------|:---------------|:--------------------|:-----------|:-------------------------------|---------------:|:--------------|:-------------|-----------------:|-----------------:|------------------------:|:-------------------|
|  0 | ferdinandmueller@google.sa    | Ap #875-3504 Non Street             | 02 38 76 93 41 | Ferdinand Mueller  | United Kingdom | Warwickshire        | Nuneaton   | 32.7627286528, -158.6625671168 |             67 | United States | 02/19/1993   |                1 |                0 |                       0 | Fri                |
|  1 | solomonmiles8893@outlook.gh   | P.O. Box 551, 1609 Pharetra. Avenue | 05 84 67 56 12 | Solomon Miles      | Indonesia      | Gorontalo           | Gorontalo  | 2.5649298432, -61.4258876416   |             64 | Vietnam       | 06/18/1963   |                0 |                0 |                       0 | Tue                |
|  2 | brennanenglish9011@google.com | 8374 Erat Av.                       | 02 66 23 25 67 | Brennan English    | Ireland        | Connacht            | Galway     | 81.577866752, -97.3228767232   |             40 | Spain         | 08/16/1953   |                0 |                0 |                       0 | Sun                |
|  3 | carlosfranklin9307@yahoo.sa   | 3048 Hendrerit Ave                  | 07 78 89 73 91 | Carlos Franklin    | China          | Zhōngnán            | Hubei      | -56.7518974976, 175.1121529856 |             86 | Italy         | 10/01/1980   |                0 |                1 |                       0 | Wed                |
|  4 | amandakennedy6014@google.sn   | 710-3003 Et St.                     | 08 18 96 14 47 | Amanda Kennedy     | Singapore      | North-East Region   | Ang Mo Kio | 63.9827079168, 61.4409061376   |             91 | Turkey        | 07/31/1998   |                0 |                0 |                       0 | Fri                |
|  5 | quintessabuchanan@icloud.net  | 660-7772 Erat Av.                   | 04 29 22 78 74 | Quintessa Buchanan | Mexico         | Coahuila            | Saltillo   | 55.9738343424, -165.1289992192 |            100 | New Zealand   | 06/01/1996   |                0 |                0 |                       0 | Sat                |
|  6 | hayeshodge5962@yahoo.couk     | 723-9741 Aliquet St.                | 06 97 34 94 74 | Hayes Hodge        | Poland         | Podlaskie           | Suwałki    | -88.375186944, -1.4612047872   |              3 | Poland        | 09/18/1975   |                0 |                0 |                       0 | Thu                |
|  7 | kennedydickson@hotmail.couk   | P.O. Box 816, 8452 Nullam Av.       | 09 37 69 90 68 | Kennedy Dickson    | Vietnam        | Hòa Bình            | Hòa Bình   | 39.1863397376, -43.223748608   |             48 | Costa Rica    | 03/09/1985   |                0 |                0 |                       0 | Sat                |
|  8 | drewvaughan@google.net        | 1038 Quis Rd.                       | 09 58 49 86 83 | Drew Vaughan       | Indonesia      | Gorontalo           | Gorontalo  | 83.861198848, -25.3758437376   |             42 | Vietnam       | 07/06/1952   |                0 |                0 |                       0 | Sun                |
|  9 | arsenioatkins@icloud.ca       | P.O. Box 483, 5503 Erat Avenue      | 04 25 44 15 97 | Arsenio Atkins     | Philippines    | Zamboanga Peninsula | Dapitan    | -11.8733601792, 161.7532027904 |             13 | Philippines   | 09/25/1968   |                0 |                0 |                       0 | Wed                |


Enjoy 🚀 🚀 🚀  !