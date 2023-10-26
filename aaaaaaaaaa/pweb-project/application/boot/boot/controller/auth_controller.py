from pweb import Blueprint

url_prefix = "/auth"
auth_controller = Blueprint(
    "auth_controller",
    __name__,
    url_prefix=url_prefix
)


@auth_controller.route("/", methods=['GET', 'POST'])
def index():
    return "Index Page"
