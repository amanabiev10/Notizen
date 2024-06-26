function showPages(noteId) {
    fetch(`/notes/${noteId}/pages/`)
        .then(response => response.json())
        .then(data => {
            var pagesList = document.getElementById('pages-list');
            pagesList.innerHTML = '';
            data.pages.forEach(page => {
                var li = document.createElement('li');
                li.textContent = page.title;
                pagesList.appendChild(li);
            });

            // Setze currentNoteId im versteckten Input-Feld
            document.getElementById('current-note-id').value = noteId;

        });
}

function addNotebook() {
    var title = document.getElementById('new-notebook-title').value.trim();
    if (title === '') {
        alert('Titel darf nicht leer sein');
        return;
    }

    $.ajax({
        url: '/notes/add_notebook/',
        method: 'POST',
        data: {
            title: title,
            csrfmiddlewaretoken: getCSRFToken()
        },
        success: function(data) {
            var li = document.createElement('li');
            li.onclick = function() {
                showPages(data.id);
            };
            li.innerHTML = '<a href="#">' + data.title + '</a>';
            document.getElementById('notebooks-list').appendChild(li);
            document.getElementById('new-notebook-title').value = '';
        },
    });
}

function addPage() {
    var title = document.getElementById('new-page-title').value.trim();
    if (title === '') {
        alert('Titel darf nicht leer sein');
        return;
    }

    var noteId = document.getElementById('current-note-id').value;
    if (!noteId) {
        alert('Erstellen Sie einen Notizbuch zuerst');
        return;
    }

    $.ajax({
        url: '/notes/add_page/',
        method: 'POST',
        data: {
            title: title,
            note_id: noteId,
            csrfmiddlewaretoken: getCSRFToken()
        },
        success: function(data) {
            var li = document.createElement('li');
            li.textContent = data.title;
            document.getElementById('pages-list').appendChild(li);
            document.getElementById('new-page-title').value = '';
        },
    });
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

