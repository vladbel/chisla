"""docstring"""
import matplotlib.pyplot as plt
import data_providers.data_provider_simple as dps
import data_structures.transaction_base as tr


TR = tr.TransactionBase("AAA", 1, 1)
DP = dps.DataProviderSimple()
plt.plot(DP.get_data())
plt.ylabel('some numbers')
plt.show()
