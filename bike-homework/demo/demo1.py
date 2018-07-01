import pandas as pd

df = pd.read_csv(r"D:\dev\self\HtmlTest\udacity\python-practise\bike-homework\demo\chicago.csv")
print(df.head())  # first 5 rows of data
# print(df.columns)
'''
Index(['Start Time', 'End Time', 'Trip Duration', 'Start Station',
       'End Station', 'User Type', 'Gender', 'Birth Year'],
      dtype='object')
'''
# print(df.describe())
'''
       Trip Duration   Birth Year
count     400.000000   330.000000
mean      938.215000  1980.533333
std      2466.972184    11.723011
min        97.000000  1949.000000
25%       407.000000  1973.000000
50%       634.000000  1984.000000
75%       997.750000  1989.000000
max     47551.000000  1999.000000
'''
# print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 8 columns):
Start Time       400 non-null object
End Time         400 non-null object
Trip Duration    400 non-null int64
Start Station    400 non-null object
End Station      400 non-null object
User Type        400 non-null object
Gender           330 non-null object
Birth Year       330 non-null float64
dtypes: float64(1), int64(1), object(6)
memory usage: 15.7+ KB
None
'''
# print(df['Trip Duration'].value_counts())
'''
721     4
280     3
335     3
237     3
509     2
770     2
667     2
660     2
1135    2
407     2
419     2
1404    2
742     2
431     2
591     2
583     2
274     2
333     2
681     2
1341    2
292     2
816     2
302     2
811     2
286     2
736     2
273     2
780     2
262     2
235     2
       ..
879     1
368     1
1394    1
883     1
760     1
373     1
467     1
1742    1
888     1
352     1
863     1
1885    1
848     1
884     1
1860    1
837     1
838     1
844     1
334     1
994     1
1873    1
348     1
336     1
339     1
852     1
344     1
1160    1
1370    1
1883    1
605     1
Name: Trip Duration, Length: 351, dtype: int64
'''
# print(df['Start Station'].unique())
'''
['Columbus Dr & Randolph St' 'Kingsbury St & Erie St'
 'Canal St & Madison St' 'Spaulding Ave & Armitage Ave'
 'Clark St & Randolph St' 'Ogden Ave & Race Ave'
 'Clinton St & Washington Blvd' 'Canal St & Adams St'
 'Wentworth Ave & Archer Ave' 'State St & Kinzie St' 'Clark St & Lake St'
 'Larrabee St & Division St' 'Ashland Ave & Division St'
 'LaSalle St & Washington St' 'Sheffield Ave & Webster Ave'
 'Orleans St & Merchandise Mart Plaza' 'Southport Ave & Irving Park Rd'
 'Central St & Girard Ave' 'Kingsbury St & Kinzie St'
 'State St & Pearson St' 'Clinton St & 18th St' 'Loomis St & Jackson Blvd'
 'Paulina Ave & North Ave' 'Wabash Ave & 16th St' 'Adler Planetarium'
 'California Ave & Milwaukee Ave' 'Sedgwick St & North Ave'
 'Oakley Ave & Irving Park Rd' 'Streeter Dr & Grand Ave'
 'Franklin St & Lake St' 'Clinton St & Roosevelt Rd' 'Theater on the Lake'
 'Broadway & Berwyn Ave' 'Clark St & Winnemac Ave' 'Wells St & Concord Ln'
 'LaSalle St & Jackson Blvd' 'Desplaines St & Jackson Blvd'
 'Peoria St & Jackson Blvd' 'Milwaukee Ave & Rockwell St'
 'Michigan Ave & Lake St' 'Clark St & Wellington Ave' 'Shedd Aquarium'
 'Michigan Ave & 8th St' 'Ashland Ave & 21st St'
 'Damen Ave & Charleston St' 'Wabash Ave & Grand Ave'
 'Cornell Ave & Hyde Park Blvd' 'Michigan Ave & 18th St'
 'Clinton St & Lake St' 'Clark St & Chicago Ave'
 'Southport Ave & Belmont Ave' 'Ellis Ave & 55th St'
 'Lincoln Ave & Fullerton Ave' 'Rush St & Cedar St'
 'Lake Shore Dr & North Blvd' 'Wabash Ave & 8th St'
 'Broadway & Waveland Ave' 'Dearborn Pkwy & Delaware Pl'
 'Sheridan Rd & Irving Park Rd' 'Lincoln Ave & Belmont Ave'
 'Lincoln Ave & Diversey Pkwy' 'Cityfront Plaza Dr & Pioneer Ct'
 'Wood St & Division St' 'Wells St & Huron St'
 'Field Blvd & South Water St' 'Morgan St & Polk St'
 'Halsted St & Roscoe St' 'Wacker Dr & Washington St'
 'Sheridan Rd & Lawrence Ave' 'Damen Ave & Grand Ave'
 'Marshfield Ave & Cortland St' 'Campbell Ave & Fullerton Ave'
 'Wilton Ave & Belmont Ave' 'Clinton St & Madison St'
 'Desplaines St & Kinzie St' 'Cottage Grove Ave & 71st St'
 'Sheffield Ave & Wrightwood Ave' 'McClurg Ct & Illinois St'
 'Stetson Ave & South Water St' 'Burnham Harbor'
 'Ravenswood Ave & Berteau Ave' 'Dusable Harbor'
 'Damen Ave & Augusta Blvd' 'Lakefront Trail & Bryn Mawr Ave'
 'Wabash Ave & Adams St' 'Franklin St & Monroe St' 'Dearborn St & Erie St'
 'Morgan St & 18th St' 'Indiana Ave & Roosevelt Rd' 'Halsted St & Polk St'
 'Green St & Madison St' 'Lake Shore Dr & Monroe St' 'Buckingham Fountain'
 'Eckhart Park' 'Halsted St & Wrightwood Ave' 'Larrabee St & Webster Ave'
 'Broadway & Granville Ave' 'Greenview Ave & Fullerton Ave'
 'Forest Ave & Chicago Ave' 'Michigan Ave & Oak St'
 'Clifton Ave & Armitage Ave' 'Clinton St & Jackson Blvd'
 'Sheffield Ave & Fullerton Ave' 'Michigan Ave & Congress Pkwy'
 'Sheridan Rd & Loyola Ave' 'Wabash Ave & Roosevelt Rd'
 'Pine Grove Ave & Irving Park Rd' 'St. Clair St & Erie St'
 'Wentworth Ave & 33rd St' 'Bissell St & Armitage Ave'
 'Ogden Ave & Chicago Ave' 'Franklin St & Chicago Ave'
 'Southport Ave & Waveland Ave' 'Clark St & Lincoln Ave'
 'State St & Randolph St' 'State St & Harrison St'
 'Glenwood Ave & Morse Ave' 'Franklin St & Jackson Blvd'
 'Lake Shore Dr & Belmont Ave' 'Clark St & Elm St' 'Daley Center Plaza'
 'LaSalle St & Adams St' 'Wells St & Evergreen Ave'
 'Sangamon St & Washington Blvd (*)' 'Southport Ave & Roscoe St'
 'Michigan Ave & Washington St' 'Loomis St & Lexington St'
 'Wells St & Walton St' 'Rush St & Superior St' 'Ritchie Ct & Banks St'
 'Chicago Ave & Sheridan Rd' 'Wilton Ave & Diversey Pkwy'
 'Canal St & Taylor St' 'MLK Jr Dr & 29th St' 'Sedgwick St & Huron St'
 'Federal St & Polk St' 'Hampden Ct & Diversey Pkwy'
 'Calumet Ave & 33rd St' 'Logan Blvd & Elston Ave'
 'Western Ave & Congress Pkwy' 'University Ave & 57th St'
 'Morgan St & Lake St' 'Sheffield Ave & Willow St'
 'Lake Shore Dr & Ohio St' 'Washtenaw Ave & Lawrence Ave'
 'Ashland Ave & Lake St' 'Broadway & Cornelia Ave' 'Rush St & Hubbard St'
 'Shore Dr & 55th St' 'Southport Ave & Wrightwood Ave'
 'Damen Ave & Cortland St' 'Ada St & Washington Blvd'
 'Marion St & South Blvd' 'Ellis Ave & 58th St' 'Michigan Ave & 14th St'
 'Racine Ave (May St) & Fulton St' 'Orleans St & Elm St (*)'
 'Broadway & Belmont Ave' 'Leavitt St & Armitage Ave'
 'Halsted St & Diversey Pkwy' 'Damen Ave & Division St'
 'Broadway & Barry Ave' 'Damen Ave & Pierce Ave' 'Green St & Randolph St'
 'Sedgwick St & Webster Ave' 'Ravenswood Ave & Balmoral Ave'
 'Montrose Harbor' 'Western Ave & Walton St' 'Western Ave & Winnebago Ave'
 'Ashland Ave & Belle Plaine Ave' 'Western Ave & Division St'
 'Wood St & Milwaukee Ave' 'Milwaukee Ave & Wabansia Ave'
 'Milwaukee Ave & Grand Ave' 'Kedzie Ave & Palmer Ct'
 'Spaulding Ave & Division St' 'Troy St & North Ave'
 'Sheffield Ave & Waveland Ave' 'Clark St & Schreiber Ave'
 'Lake Park Ave & 53rd St' 'Calumet Ave & 21st St'
 'Jefferson St & Monroe St' 'LaSalle St & Illinois St' 'Wells St & Elm St'
 'Rockwell St & Eastwood Ave' 'Michigan Ave & Jackson Blvd'
 'Fort Dearborn Dr & 31st St' 'Michigan Ave & Pearson St'
 'Dearborn St & Monroe St' 'Francisco Ave & Foster Ave'
 'Richmond St & Diversey Ave' 'Orleans St & Ohio St'
 'Halsted St & Dickens Ave' 'Southport Ave & Wellington Ave'
 'Wolcott Ave & Polk St' 'Millennium Park' 'Kimbark Ave & 53rd St'
 'Normal Ave & Archer Ave' 'Dearborn St & Adams St'
 'Campbell Ave & Montrose Ave' 'Racine Ave & Fullerton Ave'
 'Cannon Dr & Fullerton Ave' 'Wabash Ave & Wacker Pl'
 'Benson Ave & Church St' 'Wabash Ave & Cermak Rd' 'Kedzie Ave & 21st St'
 'Broadway & Wilson Ave' 'Larrabee St & Kingsbury St']
'''

# print(df['Trip Duration'].unique())