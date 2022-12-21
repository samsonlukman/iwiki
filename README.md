This project is a wikipedia-like program that displays entries on its homepage, each title is linked to
the content of the content, users can search for the entries, they also get the close match of their search.

Users can create new pages, edit pages and also save their edits.

In utils.py, there are three functions; list entries list all the entries, get_entry retrieves the title 
of an entry and returns its content like a dictionary while save_entry saves an entry given its title and markdown content.

The urls.py contains the url pathof the website; [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.user_entry, name="search"),   
    path("query/", views.query, name="query"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("random_page", views.random_page, name="random_page",)
    
]

In views.py, different functions were written dictating the backend for the website with each of them 
linked to their respective html pages for the frontend.

The index function calls the list_entries function from util.py and associates its value to a variable, 
"entries" which is linked to the index.html page where, using django, we looped through the entries and 
returned the value, "entry". we also linked all the entries on the homepage using href to the wiki/
<str:entry> path thus, once a user clicks an entry, it gives them the result.

In the wiki/<str:entry> path, we allow the user to type in any keyword into the url bar. if their search 
corresponses to entries on the website, they get the result or get an error message. The path was
linked to a function called user_entry in views.py whose results are linked to user_entry.html.
The function checks if user entry exists or not with markdown2.markdown converts the contents to html.

The query function in views.py processes a user's search and returns a value. On the website, a user can 
search for a word using the search box. We started off by checking if the user's search is in our entries 
by saying, 
if request.method == "POST":
        entry_search = request.POST['q']
        title = util.get_entry(entry_search)
        box_content = title
        if title is not None:   
            return render(request, "encyclopedia/user_entry.html", {
                "title": title,
                "box_content": markdown2.markdown(box_content)
            })
Here, the entry search stores the user's search where 'q' is the name of the user's search as in written
in layout.html. The title stores the entry_search using it as a parameter for the get_entry function
from util.py. We checked if the title or search exists and if it does, it returns our user_entry.html
with the title and a converted to html format of the box_content using markdown

If the search is not in our entry, we check for the close match using the get_close_matches from
difflib library. We wrote;
else:
            entries_list = util.list_entries()
            close_words = []
            close_match = get_close_matches(entry_search, entries_list)
            for close_match in entries_list:
                if entry_search.lower() in close_match.lower():
                    close_words.append(close_match)
            return render(request, "encyclopedia/query.html", {
                "close_words": close_words
            })

If the search is not found, we store our entries in entries_list and close_words as an empty list.
The close_metch fetches the close match from entry_search in our list of entries. Using a for loop,
we check through our entries_list if the close_match is found, if found(we converted to lower case), we
append the close_match to our close_words list and we display our query.html that returns the value
of a user's input. In the html, we used for django for loop to check the entry in close_words.

The new_page function allows a user to create a new_page and if the page title exists in our list_entries
function in util.py, it displays an error that the page exists. Otherwise, we call the save_entry
function that stores entries given its title and markdown content.

The edit_page function lets a user edit the entries while the save_edit allows the edit to be saved
once the request is post and it displayes the content of the update.

The random_page function uses random.choice from the random library and allows a user to get

