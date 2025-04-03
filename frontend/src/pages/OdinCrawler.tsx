import React, { useState } from "react";

interface CrawlerResults {
  title?: string;
  text_content?: string;
  images?: string[];
  links?: string[];
}

const OdinCrawler: React.FC = () => {
  const [keyword, setKeyword] = useState("");
  const [url, setUrl] = useState("");
  const [results, setResults] = useState<CrawlerResults | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showPopup, setShowPopup] = useState(false);

  const handleCrawl = async () => {
    if (!keyword.trim() && !url.trim()) {
      setError("⚠️ Please enter a keyword or a URL.");
      return;
    }

    setLoading(true);
    setError("");
    setResults(null);

    const requestBody: Record<string, string> = {};
    if (keyword.trim()) requestBody.keyword = keyword;
    if (url.trim()) requestBody.url = url;

    try {
      const response = await fetch("http://127.0.0.1:8000/api/crawl/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody),
      });

      const data: CrawlerResults = await response.json();
      if (!response.ok) throw new Error("❌ Failed to fetch data.");

      setResults(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "❌ Something went wrong.");
    }

    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white p-6">
      <h1 className="text-3xl font-bold mb-6">🔍 Odin Crawler</h1>
      <div className="flex flex-wrap justify-center gap-4 w-full max-w-2xl">
        <input
          type="text"
          placeholder="Enter keyword"
          className="flex-1 p-2 rounded bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        />
        <input
          type="text"
          placeholder="Enter URL"
          className="flex-1 p-2 rounded bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button
          onClick={handleCrawl}
          className="p-2 bg-blue-500 rounded hover:bg-blue-600 transition disabled:bg-gray-500"
          disabled={loading}
        >
          {loading ? "Crawling..." : "Crawl"}
        </button>
      </div>

      {error && <p className="text-red-500 mt-4">{error}</p>}

      {results && (
        <div className="w-full max-w-3xl bg-gray-800 p-6 mt-6 rounded-lg shadow-lg flex flex-col items-start">
          {results.title && <h3 className="text-xl font-bold text-blue-400">{results.title}</h3>}
          <p className="mt-4 text-gray-300">
            {results.text_content?.trim() || "No content extracted."}
          </p>
          {results.images && results.images.length > 0 && (
            <div className="mt-4">
              <h4 className="text-lg text-blue-300">🖼 Extracted Images:</h4>
              <div className="grid grid-cols-2 gap-4 mt-2">
                {results.images.map((imgSrc, index) => (
                  <img key={index} src={imgSrc} alt={`Extracted ${index}`} className="w-full h-32 object-cover rounded" />
                ))}
              </div>
            </div>
          )}
          {results.links && results.links.length > 0 && (
            <div className="mt-4">
              <h4 className="text-lg text-blue-300">🔗 Extracted Links:</h4>
              <ul className="list-disc pl-6 text-gray-300">
                {results.links.map((link, index) => (
                  <li key={index}>
                    <a href={link} target="_blank" rel="noopener noreferrer" className="text-blue-400 underline">
                      {link}
                    </a>
                  </li>
                ))}
              </ul>
              <button
                onClick={() => setShowPopup(true)}
                className="mt-4 p-2 bg-green-500 rounded hover:bg-green-600 transition"
              >
                View Extracted Links Info
              </button>
            </div>
          )}
        </div>
      )}

      {showPopup && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <div className="bg-gray-800 p-6 rounded-lg shadow-lg text-center text-white">
            <p className="text-lg font-bold">📂 File Information</p>
            <p className="mt-4">Please navigate to the <strong>Astraeus_extracted_links.csv</strong> file to view the extracted links for the specified keyword.</p>
            <button
              onClick={() => setShowPopup(false)}
              className="mt-4 p-2 bg-red-500 rounded hover:bg-red-600 transition"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default OdinCrawler;
