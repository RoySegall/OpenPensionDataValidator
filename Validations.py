from decimal import Decimal, DecimalException
import decimal
import datetime


class Validations(object):

    # The header size.
    header_size = 0

    # The columns.
    columns_count = 0

    # The number of rows.
    rows_count = 0

    # The instrument name.
    instrument = ''

    # Field name.
    field = ''

    # Define if the current value is context or not.
    is_context = False

    # The context name.
    context_name = ''

    # The name of sub spreadsheet.
    instrument_dict_validations = {
        'cash': 'מזומנים',
    }

    # Keep list of currency.
    currencies_list = [
        'דולר אוסטרליה',
        'ריאל ברזילאי',
        'דולר קנדי',
        'פרנק שוויצרי',
        'פסו ציליאני',
        'יואן סיני',
        'כתר דני',
        'אירו',
        'ליש"ט',
        'דולר הונג קונג',
        'פורינט הונגרי',
        'רופי הודי',
        'יין יפני',
        'פזו מכסיקני',
        'שקל חדש ישראלי',
        'כתר נורווגי',
        'ניו זילנד דולר',
        'זלוטי פולני',
        'רובל רוסי',
        'כתר שוודי',
        'דולר סינגפורי',
        'לירה טורקית',
        'דולר טיוואני',
        'דולר ארהב',
        'רנד דרא"פ',
        'UNKNOWN',
    ]

    _instrument_sub_type = [
        "תעודות התחייבות ממשלתיות",
        "תעודות חוב מסחריות",
        'אג"ח קונצרני'
        "מניות",
        "תעודות סל",
        "קרנות נאמנות",
        "קרנות מחקות",
        "כתבי אופציה",
        "אופציות",
        "חוזים עתידים",
        "מוצרים מובנים"
    ]

    # List of errors.
    errors = []

    def not_null(self, val):
        """
        Check if the value is none or not defined.
        """
        try:
            if val is None:
                return {'result': False, 'msg': "Invalid 'None' value"}
            if val == '':
                return {'result': False, 'msg': "Invalid empty string value"}
        except NameError:
            return {'result': False, 'msg': "undefined value"}

        return {'result': True}

    def asset_type(self, val):
        """
        Check if value is one of the asset types.
        """
        asset_types = ['הלוואות', 'ניירות ערך סחירים', 'ניירות ערך לא סחירים', 'מזומנים', 'זכויות', 'השקעות אחרות']

        if val in asset_types:
            return {'result': True}

        return {'result': False, 'msg': "unrecognized asset type"}

    def decimal_positive(self, val):
        """
        Check if value is decimal positive with 2 positions after floating point.
        """
        return self.__decimal(val, True)

    def decimal_negative(self, val):
        """
        Check if value is decimal positive with 2 positions after floating point.
        """
        return self.__decimal(val, False)

    def __decimal(self, val, is_positive=True):
        """
        Check if the variable is decimal or not.

        :param val:
            The value to check.
        :param is_positive:
            Determine if we allowed that the value can be positive or not.

        :return:
        """

        # The object with the results of the functions.
        results = {
            'result': True,
            'msg': '',
        }

        try:
            d = Decimal(str(val))

            if d.as_tuple().exponent == -2:
                sign = "positive"
                if not is_positive:
                    sign = "negative"
                    d = d * -1

                if d > 0:
                    return results
                else:
                    return {
                        'result': False,
                        'msg': "The value %s must be %s decimal" % (val, sign)
                    }
            else:
                return {
                    'result': False,
                    'msg': "The value %s must have 2 numbers after decimal point" % val
                }

        except (ValueError, DecimalException):
            return {
                'result': False,
                'msg': "The value %s not a decimal or not defined" % val
            }

    def is_positive(self, val):
        """
        Checking if the number is validate.

        :param val:
            The number to validate.
        :return:
        """
        number = float(val)
        if number > 0:
            return {'result': True}
        else:
            return {'result': False, 'msg': "Not a positive number"}

    def is_float(self, val):
        """
        Checking if the number is float.

        :param val:
            The number we need to validate.
        :return:
        """
        try:
            if val % 1 == 0:
                return {'result': False, 'msg': "Not a float"}
            else:
                return {'result': True}
        except ValueError:
            return {'result': False, 'msg': "Not a float"}

    def valid_currency(self, val):
        """
        Validating currency from a list.

        :param val:
            The currency to validate.

        :return:
        """

        if val in self.currencies_list:
            return {'result': True}

        return {'result': False, 'msg': "currency %s not recognized" % val}

    def date_format(self, val, format_to_validate='%d/%m/%Y', format_to_display='DD/MM/YYYY'):
        """
        Checking the date format.

        :param val:
            The date we need to check.
        :param format_to_validate:
            The format which we will validate.
        :param format_to_display:
            The format to display when the validation failed.

        :return:
        """
        try:
            datetime.datetime.strptime(val, format_to_validate)
            return {'result': True}
        except ValueError:
            return {'result': False, 'msg': "Incorrect date format, should be %s" % format_to_display}

    def digits_amount(self, val, min_digits, max_digits=0):
        """
        Check the amount of digits in the number.

        :param val:
            The number we need to check.
        :param min_digits:
            The min number of digits the number can hold.
        :param max_digits:
            The max number of the digits the number can hold. Optional;
        :return:
        """
        if val.length > min_digits & max_digits == 0:
            return {'result': True}

        if val.length > min_digits & val.length < max_digits:
            return {'result': True}
        # todo: better limitation handling.
        return {'result': False, 'msg': "Value exceeded digits boundary"}

    def number_in_range(self, val, min_range=0, max_range=0):
        """
        Checking the number is in the range.

        :param val:
            The number to validate.
        :param min_range:
            The min range for the number.
        :param max_range:
            The max range for the number.

        :return:
        """

        return (min_range != 0 and min_range >= val and max) and max_range != 0 and max_range <= val

    def instrument_sub_type(self, val):
        """
        Checking the value is a instrument sub type.
        :param val:
        :return:
        """
        return val in self._instrument_sub_type