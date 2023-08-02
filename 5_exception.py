# custom exception, inheriting from base Exception
class InvaidOperationError(Exception):
    pass


try:
    1/0
except InvaidOperationError as err:
    print(f"Exception: {err}")
except ValueError as err:
    print(f"Exception: {err}")
except Exception as ex:
    print(f"Exception: {ex}")
else:
    print("All iz Well !!")
finally:
    print("All Done !!")
