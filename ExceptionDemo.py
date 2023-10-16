class UserError(Exception):
            def __init__(self,message="user has done some mistake"):
                    self.message = message
                    super().__init__(self.message)

raise UserError
