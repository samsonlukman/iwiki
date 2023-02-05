from django.shortcuts import render
from difflib import get_close_matches
from . import util
import random
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def user_entry(request, entry):
    title = entry
    print(title)
    content = util.get_entry(entry)
    try:
        return render(request, "encyclopedia/user_entry.html", {
        "title": title,
        "box_content": markdown2.markdown(content)
    })

    except TypeError:
        return render(request, "encyclopedia/error.html", {
            "display": "The page you searched does not exist"
        })
    
def query(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        entry_content = util.get_entry(entry_search)
        if entry_content is not None:
            return render(request, "encyclopedia/user_entry.html", {
                "title": entry_search,
                "box_content": markdown2.markdown(entry_content)
            })
        else:
            entries_list = util.list_entries()
            close_matches = get_close_matches(entry_search, entries_list)  
            close_words = []
            for close_match in close_matches:  
                if entry_search.lower() in close_match:
                    close_words.append(close_match)
                    return render(request, "encyclopedia/query.html", {
                        "title": close_words,
                        
                    })
                
                elif entry_search.title() in close_match:
                    close_words.append(close_match)
                    return render(request, "encyclopedia/query.html", {
                        "title": close_words,
                        
                    })
                
                elif entry_search.upper() in close_match:
                    close_words.append(close_match)
                    return render(request, "encyclopedia/query.html", {
                        "title": close_words,
                        
                    })
                
            else:
                return render(request, "encyclopedia/error.html", {
                    "display": "No match found"
                })
            


        
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        box_content = request.POST['box_content']
        entry_exists = util.get_entry(title)

        if entry_exists is not None:
            return render(request, "encyclopedia/error.html", {
                "display": "Page already exists"
            })

        else:
            util.save_entry(title, box_content)
            return render(request, "encyclopedia/user_entry.html", {
                "title": title,
                "box_content": markdown2.markdown(box_content)
                
            })

def edit_page(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        box_content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "box_content" : box_content
        })


def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        box_content = request.POST['box_content']
        util.save_entry(title, box_content)
        return render(request, "encyclopedia/user_entry.html", {
            "title": title,
            "box_content": markdown2.markdown(box_content)
        } )  

def random_page(request):
    entry = util.list_entries()   
    entries = random.choice(entry)
    content = markdown2.markdown(util.get_entry(entries))

    return render(request, "encyclopedia/user_entry.html", {
        "title": entries,
        "box_content": content
    })

