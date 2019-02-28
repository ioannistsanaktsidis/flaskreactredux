from flask import Blueprint, jsonify


blueprint = Blueprint(
    'testapp_api',
    __name__,
    url_prefix='/api'
)


@blueprint.route('/health', methods=['HEAD', 'GET'])
def ping():
    """Load balancer ping view."""
    return jsonify({"health": "ok"})
