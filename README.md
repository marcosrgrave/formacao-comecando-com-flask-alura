## Formação Começando com Flask - Alura
Repository created to apply the knowledge acquired in the Alura Flask Course.

### Highlights of this Course:
- Flask + HTML Forms
- Flask + CSS (Bootstrap)
- Reusable HTML Components
- Flask Session

### Changes made:
- Applied OOP
- Used Flask Restful
- Hidden sensitive data in .env file

### Problems faced:
- For some reason, flask's render_template() function was returning string instead of HTML. To fix it, had to use of another of flask's tools, the make_response() function. It makes possible to specify the data Content-Type, witch is text/html in this case. This solution fixed the issue.
