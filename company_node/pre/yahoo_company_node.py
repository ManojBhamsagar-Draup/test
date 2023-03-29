from typing import Dict
from system.logger.factory import LoggerFactory

logger = LoggerFactory.create(name="YahooCompany")
logger_context = "YahooCompany"


def yahoo_company_preprocessor(input_doc: Dict):
    """
        removes special characters and updates company_name in input_doc
    """
    filter_set = {'Inc. & Associates',
                   'Inc. & Partners',
                   'Inc. & Sons',
                   'Inc. & Company',
                   'Plc', 'PLC & Co.',
                   'PLC & Associates',
                   'PLC & Partners',
                   'Corporation and Co.',
                   'Corporation & Associates',
                   'Corporation & Partners',
                   'Incorporated',
                   'Corp. & Co.',
                   'Corp. & Associates',
                   'Corp. & Partners',
                   'Corp. & Sons',
                   'Corp. & Company',
                   'Group Inc.',
                   'Holdings Inc.',
                   'Enterprises Inc.',
                   'International Inc.',
                   'Innovations Inc.',
                   'Solutions Inc.',
                   'Technologies Inc.',
                   'Ventures Inc.',
                   'Partners Inc.',
                   'Industries Inc.',
                   'Services',
                   'Developments',
                   'Enterprises LLC',
                   'Enterprises Ltd.',
                   'Enterprises Limited',
                   'Enterprises Group',
                   'Enterprises Corporation',
                   'Enterprises Incorp.',
                   'Enterprises Inc. & Co.',
                   'Enterprises Inc. & Associates',
                   'Enterprises Inc. & Partners',
                   'Enterprises Inc. & Sons',
                   'Enterprises Inc. & Company',
                   'Enterprises Corp.',
                   'Enterprises Corp. & Co.',
                   'Enterprises Corp. & Associates',
                   'Enterprises Corp. & Partners',
                   'Enterprises Corp. & Sons',
                   'Enterprises Corp. & Company',
                   'Corp.',
                   'Corp',
                   'Inc.',
                   'Corporation',
                   'Co.', 'LLC',
                   'Ltd.',
                   'Limited',
                   'Group',
                   'Holdings',
                   'Enterprises',
                   'International',
                   'Innovations',
                   'Solutions',
                   'Technologies',
                   'Ventures',
                   'Partners',
                   'Industries',
                   'Incorp.',
                   'Inc. & Co.',
                   'Company Ltd.',
                   'Industry',
                   'Co.',
                   'Co.,',
                   'LLC',
                   'LLC.'
                   '()'}
    company_name = input_doc.get('company_name', '')
    original_company_name = company_name
    try:
        words = company_name.split()
        result_words = [word for word in words if word not in filter_set]
        company_name = ' '.join(result_words)
    except Exception as exc:
        logger._exception_mixin(msg=f"Exception occurred while filtering keywords due to: {repr(exc)}", context=logger_context)
    input_doc.update({'company_name': company_name, 'original_company_name': original_company_name})
