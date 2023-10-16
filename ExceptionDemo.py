class UserError(Exception):
            def __init__(self,message="user has done some mistake"):
                    self.message = message
                    super().__init__(self.message)

try:
        raise UserError
except UserError as us:
        print(us.message)

