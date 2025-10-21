function buildUCSCUrl(locationNum, locationName) {
  const url = new URL('https://nutrition.sa.ucsc.edu/shortmenu.aspx');
  url.searchParams.set('sName', 'UC Santa Cruz Dining');
  url.searchParams.set('locationNum', String(locationNum));
  url.searchParams.set('locationName', locationName);
  url.searchParams.set('naFlag', '1');
  return url.toString();
}

function Halls() {
  const halls = [
    { name: "John R. Lewis & College Nine Dining Hall", locationNum: "40", locationName: "John R. Lewis & College Nine Dining Hall" },
    { name: "Cowell & Stevenson Dining Hall", locationNum: "05", locationName: "Cowell & Stevenson Dining Hall" },
    { name: "Crown & Merrill Dining Hall and Banana Joe's", locationNum: "20", locationName: "Crown & Merrill Dining Hall and Banana Joe's" },
    { name: "Porter & Kresge Dining Hall", locationNum: "25", locationName: "Porter & Kresge Dining Hall" },
    { name: "Rachel Carson & Oakes Dining Hall", locationNum: "30", locationName: "Rachel Carson & Oakes Dining Hall" },
    { name: "Oakes Cafe", locationNum: "23", locationName: "Oakes Cafe" },
    { name: "Global Village Cafe", locationNum: "46", locationName: "Global Village Cafe" },
    { name: "Owl's Nest Cafe", locationNum: "24", locationName: "Owl's Nest Cafe" },
    { name: "Slug Stop", locationNum: "51", locationName: "Slug Stop" },
    { name: "UCen Coffee Bar", locationNum: "45", locationName: "UCen Coffee Bar" },
    { name: "Stevenson Coffee House", locationNum: "26", locationName: "Stevenson Coffee House" },
    { name: "Perk Coffee Bar", locationNum: "22", locationName: "Perk Coffee Bar" },
    { name: "Porter Market", locationNum: "50", locationName: "Porter Market" },
    { name: "Merrill Market", locationNum: "47", locationName: "Merrill Market" },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-4">Dining Halls by College</h1>
        {/* JerryCheng */}

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {halls.map((hall) => (
            <a
              key={hall.name}
              href={buildUCSCUrl(hall.locationNum, hall.locationName)}
              className="block bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow"
            >
              <div className="flex items-start justify-between">
                <h2 className="text-xl font-semibold text-gray-900">{hall.name}</h2>
              </div>
              {/* Hyperlinks to each dining hall and jump buttons */}
            </a>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Halls;