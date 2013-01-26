import untangle

"""Calculates the ratio between escalators in repair and all escalators that are not working"""
def calculate_ratio():
    xml = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    doc = untangle.parse(xml);
    outages = doc.NYCOutages.outage
    number_of_outages = len(outages)
    number_of_repairs = 0
    for i in range(number_of_outages):
        if outages[i].reason.cdata == "REPAIR":
            number_of_repairs = number_of_repairs + 1

    return 1.0*number_of_repairs/number_of_outages