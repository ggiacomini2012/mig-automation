import React, { useState, useEffect } from 'react';
import { Calculator, RefreshCw, Trash2 } from 'lucide-react';

interface Product {
  id: string;
  originalPrice: number;
  discountPrice?: number;
  percentageDiscounts: number[];
  fixedDiscounts: number[];
  cashback: number;
  finalPrice: number;
  totalDiscount: number;
}

function App() {
  const [originalPrice, setOriginalPrice] = useState<string>('');
  const [discountPrice, setDiscountPrice] = useState<string>('');
  const [percentageDiscounts, setPercentageDiscounts] = useState<string>('');
  const [fixedDiscounts, setFixedDiscounts] = useState<string>('');
  const [cashback, setCashback] = useState<string>('');
  const [products, setProducts] = useState<Product[]>([]);
  const [error, setError] = useState<string>('');

  const parseCommaSeparatedNumbers = (input: string): number[] => {
    if (!input.trim()) return [];
    return input
      .split(',')
      .map(item => parseFloat(item.trim()))
      .filter(num => !isNaN(num));
  };

  const calculateFinalPrice = (product: Omit<Product, 'finalPrice' | 'totalDiscount' | 'id'>): { finalPrice: number; totalDiscount: number } => {
    let finalPrice = product.originalPrice;
    let totalDiscount = 0;

    // If discount price is provided, use it directly
    if (product.discountPrice !== undefined && product.discountPrice > 0) {
      totalDiscount = product.originalPrice - product.discountPrice;
      return { finalPrice: product.discountPrice, totalDiscount };
    }

    // Apply percentage discounts
    product.percentageDiscounts.forEach(percentage => {
      const discountAmount = finalPrice * (percentage / 100);
      finalPrice -= discountAmount;
      totalDiscount += discountAmount;
    });

    // Apply fixed discounts
    product.fixedDiscounts.forEach(fixed => {
      finalPrice -= fixed;
      totalDiscount += fixed;
    });

    // Apply cashback
    if (product.cashback > 0) {
      finalPrice -= product.cashback;
      totalDiscount += product.cashback;
    }

    // Ensure final price doesn't go below zero
    if (finalPrice < 0) {
      totalDiscount = product.originalPrice;
      finalPrice = 0;
    }

    return { finalPrice, totalDiscount };
  };

  const handleAddProduct = () => {
    if (!originalPrice || parseFloat(originalPrice) <= 0) {
      setError('Please enter a valid original price');
      return;
    }

    setError('');
    const parsedOriginalPrice = parseFloat(originalPrice);
    const parsedDiscountPrice = discountPrice ? parseFloat(discountPrice) : undefined;
    const parsedPercentageDiscounts = parseCommaSeparatedNumbers(percentageDiscounts);
    const parsedFixedDiscounts = parseCommaSeparatedNumbers(fixedDiscounts);
    const parsedCashback = cashback ? parseFloat(cashback) : 0;

    const newProduct: Omit<Product, 'finalPrice' | 'totalDiscount' | 'id'> = {
      originalPrice: parsedOriginalPrice,
      discountPrice: parsedDiscountPrice,
      percentageDiscounts: parsedPercentageDiscounts,
      fixedDiscounts: parsedFixedDiscounts,
      cashback: parsedCashback,
    };

    const { finalPrice, totalDiscount } = calculateFinalPrice(newProduct);

    setProducts(prev => [
      ...prev,
      {
        ...newProduct,
        id: Date.now().toString(),
        finalPrice,
        totalDiscount,
      },
    ]);

    // Reset input fields
    setOriginalPrice('');
    setDiscountPrice('');
    setPercentageDiscounts('');
    setFixedDiscounts('');
    setCashback('');
  };

  const handleReset = () => {
    setOriginalPrice('');
    setDiscountPrice('');
    setPercentageDiscounts('');
    setFixedDiscounts('');
    setCashback('');
    setProducts([]);
    setError('');
  };

  const handleRemoveProduct = (id: string) => {
    setProducts(prev => prev.filter(product => product.id !== id));
  };

  const getTotalPurchasePrice = (): number => {
    return products.reduce((sum, product) => sum + product.finalPrice, 0);
  };

  const getTotalDiscountApplied = (): number => {
    return products.reduce((sum, product) => sum + product.totalDiscount, 0);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-4 md:p-8">
      <div className="max-w-4xl mx-auto">
        <header className="mb-8 text-center">
          <div className="flex items-center justify-center mb-4">
            <Calculator className="w-10 h-10 text-blue-400 mr-2" />
            <h1 className="text-3xl md:text-4xl font-bold bg-gradient-to-r from-blue-400 to-teal-400 bg-clip-text text-transparent">
              Discount Calculator
            </h1>
          </div>
          <p className="text-gray-400">Calculate discounts and final prices with ease</p>
        </header>

        <div className="bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
          <h2 className="text-xl font-semibold mb-4 text-blue-300">Enter Product Details</h2>
          
          {error && <div className="bg-red-900/50 text-red-200 p-3 rounded-lg mb-4">{error}</div>}
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
              <label htmlFor="originalPrice" className="block text-sm font-medium text-gray-300 mb-1">
                Original Price ($)
              </label>
              <input
                type="number"
                id="originalPrice"
                value={originalPrice}
                onChange={(e) => setOriginalPrice(e.target.value)}
                className="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="e.g. 100"
                min="0"
                step="0.01"
              />
            </div>
            
            <div>
              <label htmlFor="discountPrice" className="block text-sm font-medium text-gray-300 mb-1">
                Discount Price ($) <span className="text-gray-500 text-xs">(Optional)</span>
              </label>
              <input
                type="number"
                id="discountPrice"
                value={discountPrice}
                onChange={(e) => setDiscountPrice(e.target.value)}
                className="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="e.g. 80"
                min="0"
                step="0.01"
              />
            </div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div>
              <label htmlFor="percentageDiscounts" className="block text-sm font-medium text-gray-300 mb-1">
                Percentage Discounts (%)
              </label>
              <input
                type="text"
                id="percentageDiscounts"
                value={percentageDiscounts}
                onChange={(e) => setPercentageDiscounts(e.target.value)}
                className="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="e.g. 10, 20, 5"
              />
            </div>
            
            <div>
              <label htmlFor="fixedDiscounts" className="block text-sm font-medium text-gray-300 mb-1">
                Fixed Discounts ($)
              </label>
              <input
                type="text"
                id="fixedDiscounts"
                value={fixedDiscounts}
                onChange={(e) => setFixedDiscounts(e.target.value)}
                className="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="e.g. 5, 15"
              />
            </div>
            
            <div>
              <label htmlFor="cashback" className="block text-sm font-medium text-gray-300 mb-1">
                Cashback ($)
              </label>
              <input
                type="number"
                id="cashback"
                value={cashback}
                onChange={(e) => setCashback(e.target.value)}
                className="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="e.g. 10"
                min="0"
                step="0.01"
              />
            </div>
          </div>
          
          <div className="flex flex-wrap gap-3">
            <button
              onClick={handleAddProduct}
              className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-6 rounded-lg transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 flex items-center"
            >
              <Calculator className="w-4 h-4 mr-2" />
              Calculate & Add
            </button>
            
            <button
              onClick={handleReset}
              className="bg-gray-700 hover:bg-gray-600 text-white font-medium py-2 px-6 rounded-lg transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50 flex items-center"
            >
              <RefreshCw className="w-4 h-4 mr-2" />
              Reset All
            </button>
          </div>
        </div>

        {products.length > 0 && (
          <div className="bg-gray-800 rounded-xl p-6 shadow-lg mb-8">
            <h2 className="text-xl font-semibold mb-4 text-blue-300">Product List</h2>
            
            <div className="overflow-x-auto">
              <table className="w-full text-sm text-left">
                <thead className="text-xs uppercase bg-gray-700 text-gray-300">
                  <tr>
                    <th className="px-4 py-3 rounded-tl-lg">#</th>
                    <th className="px-4 py-3">Original Price</th>
                    <th className="px-4 py-3">Discounts Applied</th>
                    <th className="px-4 py-3">Final Price</th>
                    <th className="px-4 py-3">Total Discount</th>
                    <th className="px-4 py-3 rounded-tr-lg">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {products.map((product, index) => (
                    <tr key={product.id} className="border-b border-gray-700 hover:bg-gray-700/50 transition-colors">
                      <td className="px-4 py-3">{index + 1}</td>
                      <td className="px-4 py-3">${product.originalPrice.toFixed(2)}</td>
                      <td className="px-4 py-3">
                        {product.discountPrice ? (
                          <span>Direct discount price: ${product.discountPrice.toFixed(2)}</span>
                        ) : (
                          <div>
                            {product.percentageDiscounts.length > 0 && (
                              <div>Percentage: {product.percentageDiscounts.join('%, ')}%</div>
                            )}
                            {product.fixedDiscounts.length > 0 && (
                              <div>Fixed: ${product.fixedDiscounts.join(', $')}</div>
                            )}
                            {product.cashback > 0 && <div>Cashback: ${product.cashback.toFixed(2)}</div>}
                            {!product.percentageDiscounts.length && !product.fixedDiscounts.length && product.cashback <= 0 && (
                              <span className="text-gray-500">None</span>
                            )}
                          </div>
                        )}
                      </td>
                      <td className="px-4 py-3 font-medium text-green-400">${product.finalPrice.toFixed(2)}</td>
                      <td className="px-4 py-3 font-medium text-blue-400">${product.totalDiscount.toFixed(2)}</td>
                      <td className="px-4 py-3">
                        <button
                          onClick={() => handleRemoveProduct(product.id)}
                          className="text-red-400 hover:text-red-300 transition-colors"
                          aria-label="Remove product"
                        >
                          <Trash2 className="w-5 h-5" />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            
            <div className="mt-6 p-4 bg-gray-700/50 rounded-lg">
              <div className="flex justify-between items-center mb-2">
                <span className="font-medium">Total Purchase Price:</span>
                <span className="text-xl font-bold text-green-400">${getTotalPurchasePrice().toFixed(2)}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="font-medium">Total Discount Applied:</span>
                <span className="text-xl font-bold text-blue-400">${getTotalDiscountApplied().toFixed(2)}</span>
              </div>
            </div>
          </div>
        )}
        
        <footer className="text-center text-gray-500 text-sm mt-8">
          <p>© 2025 Discount Calculator | Designed with ❤️</p>
        </footer>
      </div>
    </div>
  );
}

export default App;