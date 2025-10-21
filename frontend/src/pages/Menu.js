import { useState, useEffect } from 'react';

function Menu() {
  const [menuData, setMenuData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch from public folder
    fetch('/List.JSON')
      .then(response => response.json())
      .then(data => {
        console.log('Fetched data:', data);
        setMenuData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error loading JSON:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="text-center py-8">Loading...</div>;

  if (!Array.isArray(menuData) || menuData.length === 0) {
    return <div className="text-center py-8">No menu data available</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">Today's Menu</h1>
      {menuData.map((item, index) => (
        <div key={index} className="bg-white p-6 rounded-lg shadow-md mb-4">
          <h2 className="text-2xl font-bold">{item.text}</h2>
          <p className="text-gray-600">{item.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Menu;
