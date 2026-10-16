## Inner joins

Once data is neatly organized in different tables linked with foreign keys, we’re ready to use SQLite queries to join results back together. In these examples, we’ll use the joins.db database from this chapter’s GitHub directory. This small database contains the two tables we just organized, assocs and studies, with a few additional rows to illustrate some intricacies with different types of joins.

Let’s load the joins.db database:

```csv
\$ sqlite3 joins.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";".
sqlite> .mode columns
sqlite> .header on
```

Let’s take a peek at these example data:

<table><tr><td colspan="4">sqlite&gt; SELECT * FROM assocs;</td></tr><tr><td>id</td><td>study_id</td><td>trait</td><td>strongest_risk_snp</td></tr><tr><td>1</td><td>1</td><td>Asthma, hay fever</td><td>rs9273373</td></tr><tr><td>2</td><td>1</td><td>Asthma, hay fever</td><td>rs4833095</td></tr><tr><td>3</td><td>1</td><td>Asthma, hay fever</td><td>rs1438673</td></tr><tr><td>4</td><td>2</td><td>Hypertension</td><td>rs2820037</td></tr><tr><td>5</td><td>2</td><td>Crohn&#x27;s disease</td><td>rs6596075</td></tr><tr><td>6</td><td></td><td>Urate levels</td><td>rs12498742</td></tr></table>

<table><tr><td colspan="4">sqlite&gt; SELECT * FROM studies;</td></tr><tr><td>id</td><td>pubmedid</td><td>year</td><td>journal</td></tr><tr><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>2</td><td>17554300</td><td>2007</td><td>Nature</td></tr><tr><td>3</td><td>16252231</td><td>2005</td><td>Am J Hum G</td></tr></table>

By far, the most frequently used type of join used is an inner join. We would use an inner join to reunite the association results in the assocs table with the studies in the studies table. Here’s an example of the inner join notation:

<table><tr><td colspan="8">sqlite&gt; SELECT * FROM assocs INNER JOIN studies ON assocs.study_id = studies.id;</td></tr><tr><td>id</td><td>study_id</td><td>trait</td><td>strongest_risk_snp</td><td>id</td><td>pubmedid</td><td>year</td><td>journal</td></tr><tr><td>1</td><td>1</td><td>Asthma, hay fever</td><td>rs9273373</td><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>2</td><td>1</td><td>Asthma, hay fever</td><td>rs4833095</td><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>3</td><td>1</td><td>Asthma, hay fever</td><td>rs1438673</td><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>4</td><td>2</td><td>Hypertension</td><td>rs2820037</td><td>2</td><td>17554300</td><td>2007</td><td>Nature</td></tr><tr><td>5</td><td>2</td><td>Crohn&#x27;s disease</td><td>rs6596075</td><td>2</td><td>17554300</td><td>2007</td><td>Nature</td></tr></table>

Notice three important parts of this join syntax:

• The type of join (INNER JOIN). The table on the left side of the INNER JOIN statement is known as the left table and the table on the right side is known as the right table.
• The join predicate, which follows ON (in this case, it’s assocs.study\_id = stud ies.id).
• The new notation table.column we use to specify a column from a specific table. This is necessary because there may be duplicate column names in either table, so to select a particular column we need a way to identify which table it’s in.

Inner joins only select records where the join predicate is true. In this case, this is all rows where the id column in the studies table is equal to the study\_id column of the assocs table. Note that we must use the syntax studies.id to specify the column id from the table studies. Using id alone will not work, as id is a column in both assocs and studies. This is also the case if you select a subset of columns where some names are shared:

sqlite> SELECT studies.id, assocs.id, trait, year FROM assocs...> INNER JOIN studies ON assocs.study\_id = studies.id;

```txt
id           id          trait         year
--------   --------------   ---------------   ---------------
1           1           Asthma, hay fever 2013
1           2           Asthma, hay fever 2013
1           3           Asthma, hay fever 2013
2           4           Hypertension    2007
2           5           Crohn's disease 2007
```

To make the results table even clearer, use AS to rename columns:

sqlite> SELECT studies.id AS study\_id, assocs.id AS assoc\_id, trait, year...> FROM assocs INNER JOIN studies ON assocs.study\_id = studies.id;

```txt
study_id     assoc_id    trait           year
--------   --------------   ---------------   ---------------
1             1              Asthma, hay fever 2013
1             2              Asthma, hay fever 2013
1             3              Asthma, hay fever 2013
2             4              Hypertension      2007
2             5              Crohn's disease 2007
```

In both cases, our join predicate links the studies table’s primary key, id, with the study\_id foreign key in assocs. But note that our inner join only returns five columns, when there are six records in assocs:

```sql
sqlite> SELECT count(*) FROM assocs INNER JOIN studies
...> ON assocs.study_id = studies.id;
count(*)
-----------
5
sqlite> SELECT count(*) FROM assocs;
```

```txt
count(*)
--------------------------------
6
```

What’s going on here? There’s one record in assocs with a study\_id not in the studies.id column (in this case, because it’s NULL). We can find such rows using subqueries:

```sql
sqlite> SELECT * FROM assocs WHERE study_id NOT IN (SELECT id FROM studies);
id            study_id    trait         strongest_risk_snp
--------  --------------  --------------  --------------
6                  Urate levels  rs12498742
```

Likewise, there is also a record in the studies table that is not linked to any association results in the assocs table:

```sql
sqlite> SELECT * FROM studies WHERE id NOT IN (SELECT study_id FROM assocs);
id          pubmedid    year        journal
----------  ----------  ----------  ----------  -------
3         16252231   2005       Am J Hum Genet
```

When using inner joins, it’s crucial to remember that such cases will be ignored! All records where the join predicate assocs.study\_id = studies.id is not true are excluded from the results of an inner join. In this example, some records from both the left table (assocs) and right table (studies) are excluded.

## Left outer joins

In some circumstances, we want to join in such a way that includes all records from one table, even if the join predicate is false. These types of joins will leave some column values NULL (because there’s no corresponding row in the other table) but pair up corresponding records where appropriate. These types of joins are known as outer joins. SQLite only supports a type of outer join known as a left outer join, which we’ll see in this section.

![](images/page_483_image_0.jpg)

## Other Types of Outer Joins

In addition to the left outer joins we’ll discuss in this section, there are two other types of outer joins: right outer joins and full outer joins. Right outer joins are like left outer joins that include all rows from the right table. Right outer joins aren’t supported in SQLite, but we can easily emulate their behavior using left outer joins by swapping the left and right tables (we’ll see this in this section).

Full outer joins return all rows from both the left and right table, uniting records from both tables where the join predicate is true. SQLite doesn’t support full outer joins, but it’s possible to emulate full outer joins in SQLite (though this is outside of the scope of this book). In cases where I’ve needed to make use of extensive outer joins, I’ve found it easiest to switch to PostgreSQL, which supports a variety of different joins.

Left outer joins include all records from the left table (remember, this is the table on the left of the JOIN keyword). Cases where the join predicate are true are still linked in the results. For example, if we wanted to print all association records in the assocs table (regardless of whether they come from a study in the studies table), we would use:

sqlite> SELECT \* FROM assocs LEFT OUTER JOIN studies

<table><tr><td colspan="8">...&gt; ON assocs.study_id = studies.id;</td></tr><tr><td>id</td><td>study_id</td><td>trait</td><td>[...]risk_snp</td><td>id</td><td>pubmedid</td><td>year</td><td>journal</td></tr><tr><td>1</td><td>1</td><td>Asthma, hay fever</td><td>rs9273373</td><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>2</td><td>1</td><td>Asthma, hay fever</td><td>rs4833095</td><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>3</td><td>1</td><td>Asthma, hay fever</td><td>rs1438673</td><td>1</td><td>24388013</td><td>2013</td><td>J Allergy</td></tr><tr><td>4</td><td>2</td><td>Hypertension</td><td>rs2820037</td><td>2</td><td>17554300</td><td>2007</td><td>Nature</td></tr><tr><td>5</td><td>2</td><td>Crohn&#x27;s disease</td><td>rs6596075</td><td>2</td><td>17554300</td><td>2007</td><td>Nature</td></tr><tr><td>6</td><td></td><td>Urate levels</td><td>rs12498742</td><td></td><td></td><td></td><td></td></tr></table>

As this example shows (note the last record), SQLite left outer joins cover a very important use case: we need all records from the left table, but want to join on data from the right table whenever it’s possible to do so. In contrast, remember that an inner join will only return records in which the join predicate is true.

While SQLite doesn’t support right outer joins, we can emulate their behavior by swapping the left and right columns. For example, suppose rather than fetching all association results and joining on a study where a corresponding study exists, we wanted to fetch all studies, and join on an association where one exists. This can easily be done by making studies the left table, and assocs the right table in a left outer join:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
sqlite&gt; SELECT * FROM studies LEFT OUTER JOIN assocs
...&gt; ON assocs.study_id = studies.id;
id pubmedid year journal id study_id trait [...]_risk_snp
-- ------------ ---- ------------ -- ------------ --- ------------
1 24388013 2013 J Allergy 3 1 Asthma, hay fever rs1438673
1 24388013 2013 J Allergy 2 1 Asthma, hay fever rs4833095
1 24388013 2013 J Allergy 1 1 Asthma, hay fever rs9273373
2 17554300 2007 Nature 5 2 Crohn's disease rs6596075
2 17554300 2007 Nature 4 2 Hypertension rs2820037
3 16252231 2005 Am J Hum G
</div>

Again, note that the assocs’s columns id, study\_id, trait, and strongest\_risk\_snp have some values that are NULL, for the single record (with PubMed ID 16252231) without any corresponding association results in assocs.

Finally, while our example joins all use join predicates that are simply connecting assocs’s study\_id foreign key with studies’s primary key, it’s important to recognize that join predicates can be quite advanced if necessary. It’s easy to build more complex join predicates that join on multiple columns using AND and ON to link statements.

## Writing to Databases

Most bioinformatics databases are primarily read-only: we read data more often than we add new data or modify existing data. This is because data we load into a database is usually generated by a pipeline (e.g., gene annotation software) that takes input data and creates results we load in bulk to a database. Consequently, bioinformaticians need to be primarily familiar with bulk loading data into a database rather than making incremental updates and modifications. In this section, we’ll learn the basic SQL syntax to create tables and insert records into tables. Then in the next section, we’ll see how to load data into SQLite using Python’s sqlite3 module.

Because we mainly load data in bulk into bioinformatics databases once, we won’t cover tools common SQL modification and deletion operations like DROP, DELETE, UPDATE, and ALTER used to delete and modify tables and rows.

## Creating tables

The SQL syntax to create a table is very simple. Using the .schema dot command, let’s look at the statement that was used to create the table study in gwascat2table.db (execute this after connecting to the gwascat2table.db database with sqlite3 gwascat2table.db):

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
sqlite&gt; .schema study
CREATE TABLE study(
  id integer primary key,
  dbdate text,
  pubmedid integer,
</div>

```txt
author text,
date text,
journal text,
link text,
study text,
trait text,
initial_samplesize text,
replication_samplesize text
);
```

This shows the basic syntax of the CREATE TABLE command. The basic format is:

```sql
CREATE TABLE tablename(
  id integer primary key,
  column1 column1_type,
  column2 column2_type,
  ...
);
```

Each column can have one of the basic SQLite data types (text, integer, numeric, real, or blob) or none (for no type affinity). In the preceding example (and all table definitions used throughout this chapter), you’ll notice that the first column always has the definition id integer primary key. Primary keys are unique integers that are used to identify a record in a table. In general, every table you create should have primary key column, so you can unambiguously and exactly refer to any particular record. The guaranteed uniqueness means that no two rows can have the same primary key— you’ll get an error from SQLite if you try to insert a row with a duplicate primary key. Primary keys are one type of table constraint; others like UNIQUE, NOT NULL, CHECK and FOREIGN KEY are also useful in some situations but are outside of the scope of this chapter. If you’re creating multiple tables to build a complex relational database, I’d recommend getting the basic idea in this section, and then consulting a book dedicated to SQL. Thoughtfulness and planning definitely pay off when it comes to organizing a database.

Let’s create a toy SQLite database, and create a new table we’ll use in a later example:

```sql
\$ sqlite3 practice.db

sqlite> CREATE TABLE variants(
...> id integer primary key,
...> chrom text,
...> start integer,
...> end integer,
...> strand text,
...> name text);
```

Then, using the dot command .tables shows this table now exists (and you can check its schema with .schema variants if you like):

```txt
sqlite> .tables
variants
```

## Inserting records into tables

Like creating new tables, inserting records into tables is simple. The basic syntax is:

**INSERT INTO** tablename(column1, column2)

**VALUES** (value1, value2);

It’s also possible to omit the column names (column1, column2), but I wouldn’t recommend this—specifying the column names is more explicit and improves readability.

In the previous section, we learned how all tables should absolutely have a primary key. Primary keys aren’t something we need to create manually ourselves—we can insert the value NULL and SQLite will automatically increment the last primary key (as long as it’s an integer primary key) and use that for the row we’re inserting. With this in mind, let’s insert a record into the variants table we created in the previous section:

```sql
sqlite> INSERT INTO variants(id, chrom, start, end, strand, name)
...> VALUES(NULL, "16", 48224287, 48224287, "+", "rs17822931");
```

Then, let’s select all columns and rows from this table (which comprises only the record we just created) to ensure this worked as we expect:

<table><tr><td colspan="6">sqlite&gt; SELECT * FROM variants;</td></tr><tr><td>id</td><td>chrom</td><td>start</td><td>end</td><td>strand</td><td>name</td></tr><tr><td>1</td><td>16</td><td>48224287</td><td>48224287</td><td>+</td><td>rs17822931</td></tr></table>

## Indexing

While querying records in our example databases takes less than a second, complex queries (especially those involving joins) on large databases can be quite slow. Under the hood, SQLite needs to search every record to see if it matches the query. For large queries, these full table scans are time consuming, as potentially gigabytes of data need to be read from your disk. Fortunately, there’s a computational trick SQLite can use: it can index a column of a table.

A database index works much like the index in a book. Database indexes contain an sorted listing of all entries found in a particular row, alongside which row these entries can be found. Because the indexed column’s entries are sorted, it’s much faster to search for particular entries (compare searching for a word in an entire book, versus looking it up in an alphabetized index). Then, once the entry is found in the database index, it’s easy to find matching records in the table (similar to turning directly to a page where a word occurs in a book index). Indexes do come at a cost: just as book indexes add additional pages to a text, table indexes take up additional disk space. Indexes for very large tables can be quite large (something to be aware of when indexing bioinformatics data).

Creating an index for a particular table’s column is quite simple. Here, we create an index on the strongest\_risk\_snp column of the table assocs in the gwascat2table.db database:

```sql
sqlite> CREATE INDEX snp_idx ON assocs(strongest_risk_snp);
```

We can use the SQLite dot command .indices to look at all table indexes:

```txt
sqlite> .indices
snp_idx
```

This index will automatically be updated as new records are added to the table. Behind the scenes, SQLite will utilize this indexed column to more efficiently query records. The databases used in this chapter’s examples are quite small, and queries on indexed tables are unlikely to be noticeably faster.

Note that SQLite automatically indexes the primary key for each table—you won’t have to index this yourself. In addition, SQLite will not index foreign keys for you, and you should generally index foreign keys to improve the performance joins. For example, we would index the foreign key column study\_id in assocs with:

```txt
sqlite> CREATE INDEX study_id_idx ON assocs(study_id);
sqlite> .indices
snp_idx
study_id_idx
```

If, for some reason, you need to delete an index, you can use DROP INDEX:

```txt
sqlite> DROP INDEX snp_idx;
sqlite> .indices
study_id_idx
```

## Dropping Tables and Deleting Databases

Occasionally, you’ll create a table incorrectly and need to delete it. We can delete a table old\_table using:

```sql
sqlite> DROP TABLE old_table;
```

It’s also possible to modify existing tables with ALTER TABLE, but this is outside of the scope of this chapter.

Unlike SQLite and PostgreSQL, which support multiple databases, each database in SQLite is a single file. The best way to delete a database is just to delete the entire SQLite database file.

## Interacting with SQLite from Python

The SQLite command-line tool sqlite3 we’ve used in examples so far is just one way to interact with SQLite databases. The sqlite3 tool is primarily useful for extracting data from SQLite databases from a script, or quick exploration and interaction with a SQLite database. For more involved tasks such as loading numerous records into a database or executing complex queries as part of data analysis, it’s often preferable to interact with a SQLite database through an API. APIs allow you to interact with a database through an interface in your language of choice (as long as there’s an API for that language). In this section, we’ll take a quick look at Python’s excellent API.

## Connecting to SQLite databases and creating tables from Python

Python’s standard library includes the module sqlite3 for working with SQLite databases. As with all of Python’s standard library modules, [the documentation](http://bit.ly/sqlite3-doc) is thorough and clear, and should be your primary reference (using an API is largely about mastering its documentation!).

Let’s take a quick look at the basics of using this Python module. Because Python is well suited to processing data in chunks, it’s a good language to reach for when bulkloading data into a SQLite database. In contrast, while it’s certainly possible to use R to bulk-load into a SQLite database, it’s a bit trickier if the data is too large to load into the database all at once. The following script is a simple example of how we initialize a connection to a SQLite database and execute a SQL statement to create a simple table:

```python
import sqlite3

# the filename of this SQLite database
db_filename = "variants.db"

# initialize database connection
conn = sqlite3.connect(db_filename) ①

c = conn.cursor() ②

table_def = ""'\ ③
CREATE TABLE variants(
    id integer primary key,
    chrom test,
    start integer,
    end integer,
    strand text,
    rsid text);
"""

c.execute(table_def) ④
```

```txt
conn.commit() ⑤
conn.close() ⑥
```

1 First, we use the connect() function to establish a connection with the database (provided by the file in db\_filename; in this case, we’re using variants.db). con nect() returns an object with class Connection, which here we assign to conn. Connection objects have numerous methods for interacting with a database connection (the exhaustive list is presented in the Python documentation).
When interacting with a SQLite database through Python’s API, we use a Cursor object. Cursors allow us to retrieve results from queries we’ve made. In this script, we’re just executing a single SQL statement to create a table (and thus there are no results to fetch), but we’ll see more on how cursors are used later on.
This block of text is the SQL statement to create a table. For readability, I’ve formatted it across multiple lines.
To execute SQL statements, we use the execute() method of the Cursor object c. In cases where there are results returned from the database after executing a SQL statement (as with a SELECT statement that has matching records), we’ll use this cursor object to retrieve them—(we’ll see an example of this later).
We need to commit our statement, using the Connection.commit() method. This writes the changes to the SQL database.
Finally, we close our connection to the database using Connection.close().

We’ll save this script to create\_table.py. Before proceeding, let’s check that this worked. First, we run this script:

```txt
$ python create_table.py
```

This creates the variants.db SQLite database in the current directory. Let’s check that this has the correct schema:

```sql
\$ sqlite3 variants.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";".
sqlite> .tables
variants
sqlite> .schema variants
CREATE TABLE variants(
    id integer primary key,
    chrom test,
    start integer,
    end integer,
```

strand text, rsid text);

## Loading data into a table from Python

Next, we need to write code to load some data into the variants table. Included in this chapter’s directory in the GitHub repository is a tab-delimited example data file, variants.txt:

<table><tr><td colspan="5">$ cat variants.txt</td></tr><tr><td>chr10</td><td>114808901</td><td>114808902</td><td>+</td><td>rs12255372</td></tr><tr><td>chr9</td><td>22125502</td><td>22125503</td><td>+</td><td>rs1333049</td></tr><tr><td>chr3</td><td>46414946</td><td>46414978</td><td>+</td><td>rs333</td></tr><tr><td>chr2</td><td>136608645</td><td>136608646</td><td>-</td><td>rs4988235</td></tr></table>

There are a couple important considerations when bulk-loading data into a SQLite table. First, it’s important to make sure data loaded into the database is clean, has the correct data type, and missing values are converted to NULL (which are represented in Python by None). Note that while SQLite is very permissive with data types, it’s usually best to try to stick with one type per column—as mentioned earlier, this makes downstream work that utilizes data from a table much simpler.

Let’s now write a quick script to load data from the file variants.txt into our newly created table. Normally, you might fold this code into the same script that created the tables, but to prevent redundancy and simplify discussion, I’ll keep them separate. A simple script that reads a tab-delimited file, coerces each column’s data to the appropriate type, and inserts these into the variants table would look as follows:

```python
import sys
import sqlite3
from collections import OrderedDict

# the filename of this SQLite database
db_filename = "variants.db"

# initialize database connection
conn = sqlite3.connect(db_filename)
c = conn.cursor()

## Load Data
# columns (other than id, which is automatically incremented
tbl_cols = OrderedDict(["chrom", str), ("start", int), ①
            ("end", int), ("strand", str),
            ("rsid", str)])

with open(sys.argv[1]) as input_file:
    for line in input_file:
        # split a tab-delimited line
        values = line.strip().split("\t")

        # pair each value with its column name
```

```python
cols_values = zip(tbl_cols.keys(), values) ②

# use the column name to lookup an appropriate function to coerce each
# value to the appropriate type
coerced_values = [tbl_cols[col](value) for col, value in cols_values] ③

# create an empty list of placeholders
placeholders = ["?"] * len(tbl_cols) ④

# create the query by joining column names and placeholders quotation
# marks into comma-separated strings
colnames = ", ".join(tbl_cols.keys())
placeholders = ", ".join(placeholders)
query = "INSERT INTO variants(%s) VALUES (%s);"%(colnames, placeholders)

# execute query
c.execute(query, coerced_values) ⑤
```

```txt
conn.commit() # commit these inserts
conn.close()
```

0 First, we use an OrderedDict from the collections module to store each column in the table (and our variants.txt file) with its appropriate type. Functions str() and int() coerce their input to strings and integers, respectively. We use these functions to coerce data from the input data into its appropriate table type. Additionally, if the data cannot be coerced to the appropriate type, these functions will raise a loud error and stop the program.
Using the zip() function, we take a list of column names and a list of values from a single line of the tab-delimited input file, and combine them into a list of tuples. Pairing this data allows for easier processing in the next step.
3 Here, we use a Python list comprehension to extract the appropriate coercion function from tbl\_cols for each column. We then call this function on the value: this is what tbl\_cols[col](value) does. While storing functions in lists, dictionaries, or OrderedDicts may seem foreign at first, this strategy can drastically simplify code. The end result of this list comprehension is a list of values (still in the order as they appear in the input data), coerced to the appropriate type. To reduce the complexity of this example, I’ve not handled missing values (because our test data does not contain them). See the code-examples/ README.md file in this chapter’s GitHub repository for more information on this.
While we could directly insert our values into a SQL query statement, this is a bad practice and should be avoided. At the very least, inserting values directly into a SQL query statement string can lead to a host of problems with quotations in the data being interpreted as valid SQL quotations. The solution is to use parameter substitution, or parameterization. Python’s sqlite3 module supports two methods to parameterize a SQL statement. In this case, we replace the values in an INSERT statement with ?, and then pass our values directly as a list to the Cursor.execute() method. Note too that we ignore the primary key column id, as SQLite will automatically increment this for us.

Finally, we use the Cursor.execute() method to execute our SQL INSERT statement.

Let’s run this script, and verify our data was loaded:

\$ python load\_variants.py variants.txt

Then, in SQLite:

<table><tr><td colspan="6">sqlite&gt; .header on</td></tr><tr><td colspan="6">sqlite&gt; .mode column</td></tr><tr><td colspan="6">sqlite&gt; select * from variants;</td></tr><tr><td>id</td><td>chrom</td><td>start</td><td>end</td><td>strand</td><td>rsid</td></tr><tr><td>1</td><td>chr10</td><td>114808901</td><td>114808902</td><td>+</td><td>rs12255372</td></tr><tr><td>2</td><td>chr9</td><td>22125502</td><td>22125503</td><td>+</td><td>rs1333049</td></tr><tr><td>3</td><td>chr3</td><td>46414946</td><td>46414978</td><td>+</td><td>rs333</td></tr><tr><td>4</td><td>chr2</td><td>136608645</td><td>136608646</td><td>-</td><td>rs4988235</td></tr></table>

In this example, we’ve manually parsed and loaded multiple lines of a tab-delimited file into a table using Cursor.execute() and Connection.commit(). However, note that we’re only committing all of these INSERT statements at the end of the for loop. While this wouldn’t be a problem with small datasets that fit entirely in memory, for larger datasets (that may not fit entirely in memory) we need to pay attention to these technical details.

One solution is to commit after each INSERT statement, which we could do explicitly by pushing conn.commit() inside the loop. sqlite3 also supports autocommit mode (which can be enabled in sqlite.connect()), which automatically commits SQL statements. Unfortunately, using either conn.commit() or autocommit mode leads to each record being committed one at a time, which can be inefficient. To get around this limitation, Python’s sqlite3 Cursor objects have an executemany() method that can take any Python sequence or iterator of values to fill placeholders in a query. Cur sor.executemany() is the preferable way to bulk-load large quantities of data into a SQLite database. Loading data with this approach is a bit more advanced (because it relies on using generator functions), but I’ve included an example script in this chapter’s directory in the GitHub repository. Note that it’s also possible to interface Python’s csv module’s reader objects with executemany().

## R’s RSQLite Package

Like Python, R has a library to interface with SQLite databases: RSQLite. Like sqlite3, RSQLite is very easy to use. The primary difference is that RSQLite connects well with R’s dataframes. As a simple demonstration of the interface, let’s connect with the variants.db database and execute a query:

```txt
> library(RSQLite)
> sqlite <- dbDriver("SQLite")
> variants_db <- dbConnect(sqlite, "variants.db")

> dbListTables(variants_db)
[1] "variants"
> dbListFields(variants_db, "variants")
[1] "id"      "chrom"  "start"  "end"    "strand" "rsid"

> d <- dbGetQuery(variants_db, "SELECT * FROM variants;");
> head(d)
    id chrom     start       end strand      rsid
1   1 chr10 114808901 114808902      + rs12255372
2   2 chr9  22125502  22125503      + rs1333049
3   3 chr3  46414946  46414978      +       rs333
4   4 chr2 136608645 136608646      - rs4988235
> class(d)
[1] "data.frame"
```

dbSendQuery() grabs all results from a SQL statement at once—much like using fetchall() in sqlite3. RSQLite also has methods that support incrementally access ing records resulting from a SQL statement, through dbSendQuery() and fetch(). Overall, the RSQLite’s functions are similar to those in Python’s sqlite3; for further information, consult the manual.

Finally, let’s look at how to work with Python’s Cursor objects to retrieve data. We’ll step through this interactively in the Python shell. First, let’s connect to the database and initialize a Cursor:

```txt
>>> import sqlite3
>>> conn = sqlite3.connect("variants.db")
>>> c = conn.cursor()
```

Next, let’s use Cursor.execute() to execute a SQL statement:

```txt
>>> statement = ""\
... SELECT chrom, start, end FROM variants WHERE rsid IN ('rs12255372', 'rs333')
... ""

>>> c.execute(statement)
<sqlite3.Cursor object at 0x10e249f80>
```

Finally, we can fetch data from this query using the Cursor.fetchone(), Cursor.fetchmany() (which takes an integer argument of how many records to fetch), and Cursor.fetchall() methods. The benefit of the Cursor object is that it keeps track of which row’s you’ve fetched and which rows you haven’t, so you won’t accidentally double process a row. Let’s look at Cursor.fetchone():

```txt
>>> c.fetchone()
(u'chr10', 114808901, 114808902)
>>> c.fetchone()
(u'chr3', 46414946, 46414978)
>>> c.fetchone() # nothing left
>>>
```

## Dumping Databases

Finally, let’s talk about database dumps. A database dump is all SQL commands necessary to entirely reproduce a database. Database dumps are useful to back up and duplicate databases. Dumps can also be useful in sharing databases, though in SQLite it’s easier to simply share the database file (but this isn’t possible with other database engines like MySQL and PostgreSQL). SQLite makes it very easy to dump a database. We can use the sqlite3 command-line tool:

```sql
\$ sqlite3 variants.db ".dump"
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE variants(
  id integer primary key,
  chrom test,
  start integer,
  end integer,
  strand text,
  rsid text);
INSERT INTO "variants" VALUES(1,'chr10',114808901,114808902,'+','rs12255372');
INSERT INTO "variants" VALUES(2,'chr9',22125502,22125503,'+','rs1333049');
INSERT INTO "variants" VALUES(3,'chr3',46414946,46414978,'+','rs333');
INSERT INTO "variants" VALUES(4,'chr2',136608645,136608646,'-','rs4988235');
COMMIT;
```

The .dump dot command also takes an optional table name argument, if you wish to dump a single table and not the entire database. We can use database dumps to create databases:

```txt
$ sqlite3 variants.db ".dump" > dump.sql
$ sqlite3 variants-duplicate.db < dump.sql
```

This series of commands dumps all tables in the variants.db database to a SQL file dump.sql. Then, this SQL file is loaded into a new empty database variantsduplicate.db, creating all tables and inserting all data in the original variants.db database.