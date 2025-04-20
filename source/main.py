"""docstring1"""
from matplotlib import pyplot as plt
from  data_providers import data_provider_simple as dps
from  data_structures import transaction_base as tr


TR = tr.TransactionBase("AAA", 1, 1)
DP = dps.DataProviderSimple()
plt.plot(DP.get_data())
plt.ylabel('some numbers')
print(plt.__file__)
plt.show()
