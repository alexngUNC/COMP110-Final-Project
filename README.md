Stock Notebook Website Project


Description:

The website allows the user to generate a list of up to five stocks. Each stock in the list is has an associated link that leads to a table of current data about that stock. The user can also choose to view the table of the last stock they added to their list by clicking the "See Table" link or clicking the "Stock Table" tab at the top. Each time the user returns to the home page by clicking the navigational button at the top or clicks the "Clear List" button, the user's list of stocks is cleared and allows them to create a new list of stocks.


110 Programming Concepts:
Importing modules and running them to use functions and variables defined in them. Lots of global variables so they could be modified and passed between multiple Python files and displayed by the HTML files. Defining a custom Request class so that data requested from the Finnhub API could be stored in variables and a list of requests. The Request class also used operator overloading so that subscription (__getitem__ method) could be used with the new class. The Request class also had a __repr__ method so that Request objects could be represented as strings when printed to the terminal (mostly so I could keep track of what functions were being called and how information was being passed between the files). Object-oriented programming was used with the Pandas and finnhub libraries so that data could be retrieved from the Finnhub API and converted into a data frame and then into HTML code. Used loops and subscription to manipulate the list of requests so that there wasn't an error if the user entered less than five stocks or if the user wanted to clear their list.


Challenges Overcome:
How to display the stock data on the website instead of the Python REPL. The user not being able to clear their list after viewing it. The My List page being broken if the user entered less than five stocks (fixed by filling the other buttons with the last stock added). How to store the data requested from the API as a list of variables. How to pass that list of variables between the Python and HTML files. How to display the stock data as a table converted into an HTML. How to generate tables for multiple stocks. How to link the stocks in the My List page to their respective data tables. How to display a list of buttons of multiple stocks instead of just one. Immense frustration.


New Concepts Learned:
I learned that Python will add code to files that imports things I didn't want. How to pass variables between Python and HTML files. HTML and CSS styling. How HTML files send requests for functions defined in Python files to be called. The post and get methods of website pages and how to use them to call Python functions.


Member Contributions:

Zach Richardson:
Skeleton app route functions for index and my-list. Most of the HTML styling and text for the index and my-list HTML files. Connected to the finnhub API to be able to display the data in a Python REPL, but not the website. Stock input button and its functionality of passing the stock symbol entered into a variable that was used to request data about that stock. CSS styling in the static folder.

Alex Georgiev:
Made all of the buttons functional. Enabled the Python and HTML files to pass variables and data between each other. Website styling changes (text and logo). Constructed the data_finder function to retrieve stock data (by implementing Zach's code) and store each (stock data request in a list of requests that could be passed between the Python and HTML files. The data_finder function also converted the data retrieved from the finnhub API into a DataFrame, which was then converted into HTML code to be passed on to a function that displayed that code as a web page. Constructed the Request class (with operator overloads) so each request to finnhub was stored in a list. Made the "Add to List" button functional. Set up the stock table HTML pages and app routes for them. Created the Clear List button so that the user could restart the website without having to close it, kill the app, and run a new session. Set up the My List page to display a list of stocks the user inputted with each having a link to its associated HTML table. The key_rename function in the helpers.py file which converted a dictionary's keys into column names. Solved the challenges described above. The README file.


Goals Achieved:
Overcame the challenges described above. Successfully created a fully functional website that displays stock data based on a user-generated list of stocks. The website is also able to be reused with the Clear List and Home buttons.


Future Possibilities:
Displaying graphs instead of (or in addition to) tables. Implementing ML algorithms or simple regression models to predict the future price/trend of the stock. Binary classification ML model such as logistic regression to determine if the stock should be bought or sold. Completely rework the website styling so that it doesn't look like the COMP 110 website. Expand the list to include more than five stocks. Display the stock data in the list (I don't believe that is possible with the current implementation of how the stock table is generated as its own HTML file because I couldn't figure out how to import HTML code from one file to another without rewriting the original file).