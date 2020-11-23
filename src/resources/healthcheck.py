from flask.views import MethodView

from flask_smorest import Blueprint

from schemas import HealthcheckSchema


healthcheck_api = Blueprint(
    'healthcheck', 'healthcheck', url_prefix='/api/v1/healthcheck/',
    description='HealthCheck'
)


@healthcheck_api.route('/')
class HealthCheck(MethodView):

    @healthcheck_api.response(HealthcheckSchema, code=200)
    def get(self):
        return {'status': 'healthy'}
