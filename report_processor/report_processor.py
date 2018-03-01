import os
import glob
import pandas as pd
import dateutil.parser
from .bismarck_report import BismarckReport


class ReportProcessor(BismarckReport):

    def __init__(self):
        pass

    def get_report(self, report_file_name):
        b_report = BismarckReport
        pandas_excel = pd.ExcelFile(report_file_name)

        b_report_metadata = self.get_report_metadata(report_file_name, pandas_excel)

        # Loop over all the sheets in the file
        for sheet_name in pandas_excel.sheet_names:
            if sheet_name not in ('סכום נכסי הקרן'):
                self.get_sheet_data(pandas_excel, sheet_name)

        return BismarckReport

    def get_report_metadata(self, report_file_name, pandas_excel):
        """
        example for metadata dict structure:
        {
            'file_name': '',
            'managing_body': '',
            'year': '',
            'month': '',
            'quarter': '',
            'file_level_results': []
        }
        :param pandas_excel:
        :return: dict of above structure
        """

        meta_data = {}
        meta_data['file_name'] = os.path.basename(report_file_name)

        return {
            'file_name': '',
            'managing_body': '',
            'year': '',
            'month': '',
            'quarter': '',
            'file_level_results': []
        }

    """ 
    
    private functions 
     
    """
    def get_sheet_data(self, pandas_excel, sheet_name):
        pass

    def _calculate_rows_to_skip(self, xls_file, sheet_name):
        """ ToDo - refactor the function for current class """
        rows_to_skip_calculated = 0

        while rows_to_skip_calculated < 10:
            pre_sheet = xls_file.parse(sheet_name, skiprows=rows_to_skip_calculated)
            pre_sheet_columns = list()

            # Something
            if len(pre_sheet.columns) > 0:
                pre_sheet_columns = list(pre_sheet.columns.str.strip())

            # Something
            if ('שם נ"ע' in pre_sheet_columns) or \
                    ('שם המנפיק/שם נייר ערך' in pre_sheet_columns) or \
                    ('שם נייר ערך' in pre_sheet_columns) or \
                    ('מזומנים ושווי מזומנים' in pre_sheet_columns) or \
                    ('מספר נ"ע' in pre_sheet_columns) or \
                    ('זכויות במקרעין' in pre_sheet_columns):
                return rows_to_skip_calculated

            # Move to the next row
            rows_to_skip_calculated += 1

        return rows_to_skip_calculated

    def read_sheet(self, xls_file, sheet_name):
        # Loop over all the sheets in the file
        for sheet_name in xls_file.sheet_names:
            if sheet_name not in ('סכום נכסי הקרן'):
                read_sheet(xls_file, sheet_name, split_filename[0], quarter)

        print('Finish with {filename}'.format(filename=filename))

    # --------------------------------
    # ------ Old Code to be remove ---
    # --------------------------------
    def read_sheet(self, xls_file, sheet_name, managing_body, quarter):

        """ ToDo - refactor the function for current class """
        managing_body = ''
        quarter = ''
        rows_to_skip = self._calculate_rows_to_skip(xls_file, sheet_name)
        sheet = xls_file.parse(sheet_name, skiprows=rows_to_skip, parse_cols=40)
        sheet.columns = sheet.columns.str.strip()

        # Read the content of the sheet
        try:
            current_sh = sheet['שם המנפיק/שם נייר ערך']
        except KeyError:
            try:
                current_sh = sheet['שם נייר ערך']
            except KeyError:
                try:
                    current_sh = sheet['שם נ"ע']
                except KeyError:
                    try:
                        current_sh = sheet['מספר הנייר']
                    except KeyError:
                        try:
                            current_sh = sheet['מספר נ"ע']
                        except KeyError:
                            current_sh = sheet['אופי הנכס']

        for index, col_title in enumerate(current_sh):
            sheet_name = str(sheet_name).strip().replace('-', ' - ').replace('  ', ' ')

            if col_title == 'nan':
                continue
            elif col_title == 'בישראל':
                context = 'IL'
            elif col_title == 'בחו"ל':
                context = 'ABR'

            elif 'ישראל' in str(col_title):
                context = 'IL'
            elif 'חו"ל' in str(col_title):
                context = 'ABR'

            # Continue only if we have a context
            try:
                context
            except UnboundLocalError as e:
                continue

            # Check if it's a title or real data
            cell = is_title_per_sheet[sheet_name]

            try:
                str(sheet[cell][index])
            except KeyError:
                cell = 'מספר ני"ע'

            if str(sheet[cell][index]) == 'nan' or '*' in str(col_title) \
                    or 'סה"כ' in str(col_title) or '0' == str(col_title).strip():
                # print("This is a title row, I'm going out!")
                continue

            try:

                issuer_id = sheet['מספר ני"ע'][index]
                if str(issuer_id) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                try:
                    issuer_id = sheet['מספר הנייר'][index]
                    if str(issuer_id) == 'nan':
                        raise (KeyError)
                except KeyError as e:
                    issuer_id = sheet_name

                issuer_id = sheet_name

            try:
                rating = sheet['דירוג'][index]
                if str(rating) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                rating = ''

            try:
                rating_agency = sheet['שם מדרג'][index]
                if str(rating_agency) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                rating_agency = ''

            try:
                currency = sheet['סוג מטבע'][index]
                if str(currency) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                currency = ''

            try:
                interest_rate = sheet['שיעור ריבית'][index]
                if str(interest_rate) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                interest_rate = 0.0

            try:
                yield_to_maturity = sheet['תשואה לפידיון'][index]
                if str(yield_to_maturity) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                yield_to_maturity = 0.0

            try:
                market_cap = sheet['שווי שוק'][index]
                if str(market_cap) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                market_cap = 0.0

            try:
                rate_of_investment_channel = sheet['שעור מנכסי אפיק ההשקעה'][index]
                if str(rate_of_investment_channel) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                rate_of_investment_channel = 0.0

            try:
                rate_of_fund = sheet['שעור מסך נכסי השקעה'][index]
                if str(rate_of_fund) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                rate_of_fund = 0.0

            try:
                trading_floor = sheet['זירת מסחר'][index]
                if str(trading_floor) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                trading_floor = ''

            try:
                date_of_purchase = sheet['תאריך רכישה'][index]
                if str(date_of_purchase) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                date_of_purchase = ''

            try:
                average_of_duration = sheet['מח"מ'][index]
                if str(average_of_duration) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                average_of_duration = 0.0

            try:
                rate = sheet['שער'][index]
                if str(rate) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                rate = 0.0

            try:
                rate_of_ipo = sheet['שעור מערך נקוב מונפק'][index]
                if str(rate_of_ipo) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                rate_of_ipo = 0.0

            try:
                informer = sheet['ספק מידע'][index]
                if str(informer) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                informer = ''

            try:
                fair_value = sheet['שווי הוגן'][index]
                if str(fair_value) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                fair_value = 0.0

            try:
                activity_industry = sheet['ענף מסחר'][index]
                if str(activity_industry) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                activity_industry = ''

            try:
                if isinstance(sheet['תאריך שערוך אחרון'][index], str):
                    if len(sheet['תאריך שערוך אחרון'][index]) > 3:
                        date_of_revaluation = dateutil.parser.parse(sheet['תאריך שערוך אחרון'][index])
                    else:
                        date_of_revaluation = timezone.now()
                else:
                    date_of_revaluation = sheet['תאריך שערוך אחרון'][index]

                if str(date_of_revaluation) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                date_of_revaluation = timezone.now()

            try:
                type_of_asset = sheet['אופי הנכס'][index]
                if str(type_of_asset) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                type_of_asset = ''

            try:
                return_on_equity = sheet[''][index]
                if str(return_on_equity) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                return_on_equity = 0.0

            try:
                liabilities = sheet['סכום ההתחייבות'][index]
                if str(liabilities) == 'nan':
                    raise KeyError
            except KeyError as e:
                liabilities = 0.0

            try:

                if isinstance(sheet['תאריך סיום ההתחייבות'][index], str):
                    if 'מועד' in str(sheet['תאריך סיום ההתחייבות'][index]):
                        expiry_date_of_liabilities_pre = None
                    else:

                        try:
                            expiry_date_of_liabilities_pre = dateutil.parser.parse(
                                sheet['תאריך סיום ההתחייבות'][index],
                                fuzzy=True,
                            )
                        except ValueError:
                            print(sheet['תאריך סיום ההתחייבות'][index])
                            expiry_date_of_liabilities_pre = None
                else:
                    expiry_date_of_liabilities_pre = sheet['תאריך סיום ההתחייבות'][index]

                expiry_date_of_liabilities = expiry_date_of_liabilities_pre
                if str(expiry_date_of_liabilities) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                expiry_date_of_liabilities = timezone.now()

            try:
                effective_rate = sheet['ריבית אפקטיבית'][index]
                if str(effective_rate) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                effective_rate = 0.0

            try:
                coordinated_cost = sheet['עלות מתואמת'][index]
                if str(coordinated_cost) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                coordinated_cost = 0.0

            try:
                underlying_asset = sheet['נכס הבסיס'][index]
                if str(underlying_asset) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                underlying_asset = 0.0

            try:
                consortium = sheet['קונסורציום כן/לא'][index]
                if str(consortium) == 'nan':
                    raise (KeyError)
                elif str(consortium).strip() == 'כן':
                    consortium = True
                elif str(consortium).strip() == 'לא':
                    consortium = False
            except KeyError as e:
                consortium = False

            try:
                average_rate = sheet['שיעור ריבית ממוצע'][index]
                if str(average_rate) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                average_rate = 0.0

            try:
                par_value = sheet['שווי משוערך'][index]
                if str(par_value) == 'nan':
                    raise (KeyError)
            except KeyError as e:
                par_value = 0.0

            try:

                instrument, created = Instrument.objects.get_or_create(
                    issuer_id=issuer_id,
                    rating=rating,
                    rating_agency=rating_agency,
                    currency=currency,
                    interest_rate=interest_rate,
                    yield_to_maturity=yield_to_maturity,
                    market_cap=market_cap,
                    rate_of_investment_channel=rate_of_investment_channel,
                    rate_of_fund=rate_of_fund,
                    trading_floor=trading_floor,
                    date_of_purchase=date_of_purchase,
                    average_of_duration=average_of_duration,
                    rate=rate,
                    rate_of_ipo=rate_of_ipo,
                    informer=informer,
                    fair_value=fair_value,
                    activity_industry=activity_industry,
                    date_of_revaluation=date_of_revaluation,
                    type_of_asset=type_of_asset,
                    return_on_equity=return_on_equity,
                    liabilities=liabilities,
                    expiry_date_of_liabilities=expiry_date_of_liabilities,
                    effective_rate=effective_rate,
                    coordinated_cost=coordinated_cost,
                    underlying_asset=underlying_asset,
                    consortium=consortium,
                    average_rate=average_rate,
                    par_value=par_value,
                    managing_body=managing_body_dict[managing_body],
                    geographical_location=context,
                    instrument_sub_type=instrument_dict[sheet_name],

                    quarter=quarter[0],
                )

                print('created', instrument, created)

            except ValueError as e:

                print('index', index)
                print('issuer_id', issuer_id)
                print('rating', rating)
                print('rating_agency', rating_agency)
                print('currency', currency)
                print('interest_rate', interest_rate)
                print('yield_to_maturity', yield_to_maturity)
                print('market_cap', market_cap)
                print('rate_of_investment_channel', rate_of_investment_channel)
                print('rate_of_fund', rate_of_fund)
                print('trading_floor', trading_floor)
                print('date_of_purchase', date_of_purchase)
                print('average_of_duration', average_of_duration)
                print('rate', rate)
                print('rate_of_ipo', rate_of_ipo)
                print('informer', informer)
                print('fair_value', fair_value)
                print('activity_industry', activity_industry)
                print('date_of_revaluation', date_of_revaluation)
                print('type_of_asset', type_of_asset)
                print('return_on_equity', return_on_equity)
                print('liabilities', liabilities)
                print('expiry_date_of_liabilities', expiry_date_of_liabilities)
                print('effective_rate', effective_rate)
                print('coordinated_cost', coordinated_cost)
                print('underlying_asset', underlying_asset)
                print('consortium', consortium)
                print('average_rate', average_rate)
                print('par_value', par_value)
                print('managing_body', managing_body_dict[managing_body])
                print('geographical_location', context)
                print('instrument_sub_type', instrument_dict[sheet_name])
                print('--------------------')
                raise (ValueError)

        print('Finish with {sheet_name}'.format(sheet_name=sheet_name))