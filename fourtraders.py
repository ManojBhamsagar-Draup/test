from framework.scraper_engine.handlers.post_processor.interface import IPostProcessor
from framework.scraper_engine.types import *
from system.logger.factory import LoggerFactory

logger = LoggerFactory.create(name='FourTraders')


class FourTradersCompanyOutputTransformer(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        try:
            final_output = self.four_traders_company(data, output.main_response_props.get('response_props', {}).get('url'))
            self.extracted_data.data = final_output
        except Exception as e:
            logger._exception_mixin(msg=f"post processing failed for four traders company with exception: {e}",
                                    context=self)

    def four_traders_company(self, data, url):
        data = data[0]
        fourTradersDict = {'url': url, 'company': {}, 'responseProps': data.get('responseProps')}
        info = self.get_data_in_list(data.get('data')) if data.get('data') else []
        spr, spb, man, eq, shares, hold = [], [], [], [], [], []
        for t in info:
            if 'Sales per Business'.lower() in t.get('title').lower():
                spb = t.get('data')
            elif 'Sales per Region'.lower() in t.get('title').lower():
                spr = t.get('data')
            elif 'Managers'.lower() in t.get('title').lower():
                man = t.get('data')
            elif 'Equities'.lower() in t.get('title').lower():
                eq = t.get('data')
            elif 'Shareholders'.lower() in t.get('title').lower():
                shares = t.get('data')
            elif 'Holdings'.lower() in t.get('title').lower():
                hold = t.get('data')
        salesPerReg = self.get_sales_per_region_data(spr, url) if spr else []
        salesPerBuz = self.get_sales_per_business_data(spb, url) if spb else []
        managers = self.get_managers(man, url) if man else []
        equity = self.get_equities(eq, url) if eq else []
        shareholders = self.get_shares(shares, url) if shares else []
        holdings = self.get_holders(hold, url) if hold else []

        company = {'summary': data.get('summary'), 'noOfEmployees': data.get('no_of_employees'),
                   'name': data.get('company_name'), 'salesPerBusinesses': salesPerBuz, 'salesPerRegions': salesPerReg,
                   'managers': managers, 'equities': equity, 'holdings': holdings,
                   'marketAndIndexes': self.get_market(data.get('market')),
                   'stockExchangeCodes': self.get_stock(data.get('market')),
                   'companyContactInformation': data.get('contact'),
                   'sector': self.get_sectors(data.get('sectors')) if data.get('sectors') else None,
                   'shareholders': shareholders}

        fourTradersDict['company_name'] = data.get('company_name')
        fourTradersDict['company_ticker'] = self.get_company_ticker(data.get('company_ticker'))
        fourTradersDict['company_exchange'] = data.get('company_exchange')
        fourTradersDict['company'] = company
        fourTradersDict['detail_url'] = url
        return [fourTradersDict]

    @staticmethod
    def get_data_in_list(data):
        final_list = []
        for info in data:
            values_data = []
            final_data = {}
            final_data['title'] = info.get('title')
            if info.get('values'):
                for value in info.get('values'):
                    for data_ in value.get('final_data'):
                        values_data.append(data_.get('value'))
            final_list.append(final_data)
            final_data['data'] = values_data
        return final_list

    @staticmethod
    def get_market(market):
        return market[0].get('value')[1:].replace('-', ',') if market else None

    @staticmethod
    def get_sectors(sectors):
        sectors_list = []
        for sector in sectors:
            sectors_list.append(sector.get('value'))
        return sectors_list

    @staticmethod
    def get_stock(stock):
        if type(stock) == list and len(stock) >= 2:
            return stock[1].get('value')[1:].replace('-', ',') if stock else None
        return None

    @staticmethod
    def get_company_ticker(ticker):
        return ticker.split("(").pop().split(")")[0] if ticker else None

    def get_holders(self, hold, url):
        holdings = []
        hold_iter = [tuple(hold[4:][i:i + 4]) for i in range(0, len(hold[4:]), 4)]
        for h in hold_iter:
            try:
                holdings.append({'name': h[0], 'equities': h[1], 'percent': h[2], 'valuation': h[3]})
            except Exception as e:
                logger._warning_mixin(msg='Holders {0}, {1}'.format(url, str(e)), context=self)
                continue
        return holdings

    def get_shares(self, shares, url):
        shareholders = []
        share_iter = [tuple(shares[3:][i:i + 3]) for i in range(0, len(shares[3:]), 3)]
        for s in share_iter:
            try:
                shareholders.append({'name': s[0], 'equities': s[1], 'percent': s[2]})
            except Exception as e:
                logger._warning_mixin(msg='Shareholder {0}, {1}'.format(url, str(e)), context=self)
                continue
        return shareholders

    def get_managers(self, man, url):
        managers = []
        man_iter = [tuple(man[4:][i:i + 4]) for i in range(0, len(man[4:]), 4)]
        for m in man_iter:
            try:
                managers.append({'name': m[0], 'age': m[2], 'since': m[3], 'title': m[1]})
            except Exception as e:
                logger._warning_mixin(msg='Managers {0}, {1}'.format(url, str(e)), context=self)
                continue
        return managers

    def get_equities(self, eq, url):
        equity = []
        del eq[:6]
        eq_iter = [tuple(eq[i:i + 8]) for i in range(0, len(eq), 8)]
        for n, e in enumerate(eq_iter):
            try:
                temp = {'share': e[0], 'vote': e[1], 'quantity': e[2], 'floatValue': e[3], 'floatPercent': e[4],
                        'companyOwnedSharesValue': e[5], 'companyOwnedSharesPercent': e[6]}
                if n == 0:
                    temp['totalFloat'] = e[7]
                else:
                    temp['totalFloat'] = eq_iter[0][7]
                equity.append(temp)
            except Exception as e:
                logger._warning_mixin(msg='Equity {0}, {1}'.format(url, str(e)), context=self)
                continue
        return equity

    def get_sales_per_region_data(self, spr, url):
        salesPerReg = []
        currency_spr = spr[-1]
        del spr[-1]
        if len(spr[2]) == 4:
            info = spr[1:4]
            del spr[:3]
            spr_iter = [tuple(spr[1:][i:i + 6]) for i in range(0, len(spr[1:]), 6)]
            for n, dat in enumerate(spr_iter):
                try:
                    temp1 = {'year': info[0], 'currencySymbol': currency_spr, 'currencyValue': dat[1],
                             'percentageSymbol': dat[2][-1], 'percentageValue': dat[2]}
                    temp2 = {'year': info[1], 'currencySymbol': currency_spr, 'currencyValue': dat[3],
                             'percentageSymbol': dat[4][-1], 'percentageValue': dat[4]}
                    main = {'DomainName': dat[0], 'DeltaValue': dat[5], 'data': []}
                    main['data'].append(temp1)
                    main['data'].append(temp2)
                    salesPerReg.append(main)
                except Exception as e:
                    logger._warning_mixin(msg='Sales per buz {0}, {1}'.format(url, str(e)), context=self)
                    continue
        else:
            spr_iter = [tuple(spr[2:][i:i + 3]) for i in range(0, len(spr[2:]), 3)]
            for n, dat in enumerate(spr_iter):
                try:
                    temp = {'year': spr[0], 'currencySymbol': currency_spr, 'currencyValue': dat[1],
                            'percentageSymbol': dat[2][-1], 'percentageValue': dat[2]}
                    main = {'DomainName': dat[0], 'DeltaValue': '', 'data': []}
                    main['data'].append(temp)
                    salesPerReg.append(main)
                except Exception as e:
                    logger._warning_mixin(msg='Sales per buz {0}, {1}'.format(url, str(e)), context=self)
                    continue

        return salesPerReg

    def get_sales_per_business_data(self, spb, url):
        salesPerBuz = []
        currency_spb = spb[-1]
        del spb[-1]
        if len(spb[2]) == 4:
            info = spb[1:4]
            del spb[:3]
            spb_iter = [tuple(spb[1:][i:i + 6]) for i in range(0, len(spb[1:]), 6)]
            for n, dat in enumerate(spb_iter):
                try:
                    temp1 = {'year': info[0], 'currencySymbol': currency_spb, 'currencyValue': dat[1],
                             'percentageSymbol': dat[2][-1], 'percentageValue': dat[2]}
                    temp2 = {'year': info[1], 'currencySymbol': currency_spb, 'currencyValue': dat[3],
                             'percentageSymbol': dat[4][-1], 'percentageValue': dat[4]}
                    main = {'DomainName': dat[0], 'DeltaValue': dat[5], 'data': []}
                    main['data'].append(temp1)
                    main['data'].append(temp2)
                    salesPerBuz.append(main)
                except Exception as e:
                    logger._warning_mixin(msg='Sales per buz {0}, {1}'.format(url, str(e)), context=self)
                    continue
        else:
            spb_iter = [tuple(spb[2:][i:i + 3]) for i in range(0, len(spb[2:]), 3)]
            for n, dat in enumerate(spb_iter):
                try:
                    temp = {'year': spb[0], 'currencySymbol': currency_spb, 'currencyValue': dat[1],
                            'percentageSymbol': dat[2][-1], 'percentageValue': dat[2]}
                    main = {'DomainName': dat[0], 'DeltaValue': '', 'data': []}
                    main['data'].append(temp)
                    salesPerBuz.append(main)
                except Exception as e:
                    logger._warning_mixin(msg='Sales per buz {0}, {1}'.format(url, str(e)), context=self)
                    continue
        return salesPerBuz


class FourTradersFinancialsOutputTransformer(IPostProcessor):
    POST_PROCESSOR_TYPE = PostProcessorTypes.custom

    def process(self, *args, **kwargs):
        output: TemplateExtractorOutput = self.extracted_data
        data = output.data
        try:
            final_output = self.four_traders_financials(data, output.main_response_props.get('response_props', {}).get('url'))
            self.extracted_data.data = final_output
        except Exception as e:
            logger._exception_mixin(msg=f"post processing failed for four traders financials with exception: {e}",
                                    context=self)

    def four_traders_financials(self, data, url):
        finalDataObj = {'aboutFinancials': {}, 'companyName': None, 'financialsUrl': url,
                        'hashcodeAboutFinancials': None, 'responseProps': None}
        info = data[0]
        companyName = info.get('company_name').replace("\n", " ") if info.get('company_name') else None
        dataObj = {'companyName': companyName, 'annualIncomeStatementData': {}}
        dataObj['annualIncomeStatementData']['domainData'] = {}
        dataObj['annualIncomeStatementData']['announcementData'] = []
        finalDataObj['response_props'] = info.get('responseProps')
        resp = info.get('data')
        if resp:
            aes = resp[-1].get('values', [])[0].get('value').split('\n') if resp[-1].get('values', []) else None
            fiscal_period = resp[0].get('values', [])[0].get('value') if resp[0].get('values', []) else None
            final_data = self.get_data_in_list(resp)
            years = final_data[0].get('values')
            announcement_years = final_data[-2].get('values')
            domainData = self.get_domain_data(aes, final_data, announcement_years, fiscal_period, years)
            announcementData = self.get_announcement_dates(announcement_years, years)
            dataObj['annualIncomeStatementData']['domainData'] = domainData
            dataObj['annualIncomeStatementData']['announcementData'] = announcementData
            finalDataObj['aboutFinancials'] = dataObj
            finalDataObj['companyName'] = companyName
            finalDataObj['hashcodeAboutFinancials'] = hash(str(dataObj))
        return [finalDataObj]

    @staticmethod
    def get_domain_data(aes, final_data, announcement_years, fiscal_period, years):
        domainData = []
        for i, row in enumerate(final_data[1:-2]):
            domainDataObj = {'domainName': row.get('title'), 'data': []}
            tds = row.get('values')
            for j, td in enumerate(tds):
                data = {'annualIncomeCurrencyType': aes[0].split('in').pop(0).strip()[2:], 'estimated': False}
                if announcement_years and len(announcement_years[j]) > 1:
                    data['estimated'] = True
                if domainDataObj['domainName'][-1] == '1':
                    data['annualIncomeType'] = aes[0][1:]
                elif domainDataObj['domainName'][-1] == '2':
                    data['annualIncomeType'] = aes[1][1:]
                else:
                    data['annualIncomeType'] = 'number'
                data['year'] = years[j]
                data['fiscalPeriod'] = fiscal_period.split(" ")[-1] if fiscal_period else None
                data['value'] = td
                domainDataObj['data'].append(data)
            if domainDataObj['domainName'][-1] == '1' or domainDataObj['domainName'][-1] == '2':
                domainDataObj['domainName'] = domainDataObj['domainName'][:-1]
            domainData.append(domainDataObj)
        return domainData

    @staticmethod
    def get_announcement_dates(announcement_years, years):
        announcementData = []
        for j, td in enumerate(announcement_years):
            announcementData.append({'year': years[j], 'announcementDate': td})
        return announcementData

    @staticmethod
    def get_data_in_list(data):
        final_list = []
        for info in data:
            values = []
            title = info.get('values')[0].get('value')
            for value in info.get('values')[1:]:
                values.append(value.get('value'))
            final_list.append({'title': title, 'values': values})
        return final_list


