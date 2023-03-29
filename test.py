fiter_list = {'Inc. & Associates',
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

company_names = ["United Natural Foods, Incorporated (UNFI)",
                 "Postal Savings Bank of China (PSBC)",
                 "Lifan Industry (Group) Co., Ltd.",
                 "Qatar Islamic Bank (QIB)",
                 "SF Express (Group) Co., Ltd."]

for company_name in company_names:
    words = company_name.split()
    result_words = [word for word in words if word not in fiter_list]
    result_string = ' '.join(result_words)
    print(result_string)

