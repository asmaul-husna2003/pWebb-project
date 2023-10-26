from pweb import Blueprint
from pweb_form_rest import ssr_ui_render

url_prefix = "/"
husna_controller = Blueprint(
    "husna_controller",
    __name__,
    url_prefix=url_prefix
)


@husna_controller.route("/husna", methods=['GET', 'POST'])
def husna():
    return ssr_ui_render(view_name="husna/index")
