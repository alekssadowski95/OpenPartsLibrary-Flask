class Routes:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/api/create-part')
        def api_create_part():
            return "create part ok"
        @self.app.route('/api/read-part')
        def api_read_part():
            return "read part ok"
        @self.app.route('/api/update-part')
        def api_update_part():
            return "update part ok"
        @self.app.route('/api/delete-part')
        def api_delete_part():
            return "delete part ok"
        @self.app.route('/api/read-all-parts')
        def api_read_all_parts():
            return "read all parts ok"
        @self.app.route('/')
        def home():
            return 'OpenPartsLibrary Flask API is running!'
        