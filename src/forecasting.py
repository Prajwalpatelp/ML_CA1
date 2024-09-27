from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

class ForecastingModel:
    def __init__(self, data):
        """Initialize with historical inventory data"""
        self.data = data
    
    def train_forecasting_model(self):
        """Train a stock forecasting model using TPOT"""
        X = self.data.drop('Stock_Quantity', axis=1)
        y = self.data['Stock_Quantity']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Create TPOT Regressor for AutoML
        tpot = TPOTRegressor(verbosity=2, generations=5, population_size=20)
        tpot.fit(X_train, y_train)

        print(f"Test score: {tpot.score(X_test, y_test)}")
        tpot.export('best_pipeline.py')

        return tpot
