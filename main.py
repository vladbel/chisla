"""docstring"""
import matplotlib.pyplot as plt
import data_providers.data_provider_simple as dps


DP = dps.DataProviderSimple()
plt.plot(DP.get_data())
plt.ylabel('some numbers')
plt.show()
