import { useState } from "react";
import axios from "axios";

function App() {
  const [image, setImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image || !question) {
      alert("Please upload an image and ask a question");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);
    formData.append("question", question);

    try {
      setLoading(true);
      const res = await axios.post("http://localhost:8000/api/ask", formData);
      setAnswer(res.data.answer || "No response");
    } catch (err) {
      setAnswer("Error: " + (err.response?.data?.error || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 p-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-white mb-4">
            🧠 Visual AI Assistant
          </h1>
          <p className="text-white/80 text-lg">
            Upload an image and ask me anything about it
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Left Column - Upload and Question */}
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Image Upload Area */}
              <div className="relative">
                <div className="border-2 border-dashed border-white/40 rounded-xl p-4 text-center cursor-pointer hover:border-white/60 transition-colors">
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageChange}
                    className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                  />
                  {imagePreview ? (
                    <img
                      src={imagePreview}
                      alt="Preview"
                      className="max-h-48 mx-auto rounded-lg"
                    />
                  ) : (
                    <div className="text-white py-8">
                      <p>📸 Drop your image here</p>
                      <p className="text-sm text-white/60 mt-2">
                        or click to browse
                      </p>
                    </div>
                  )}
                </div>
              </div>

              {/* Question Input */}
              <div>
                <input
                  type="text"
                  placeholder="Ask a question about the image..."
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  className="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/30"
                />
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className="w-full bg-white/20 hover:bg-white/30 text-white font-semibold py-3 px-6 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <span className="flex items-center justify-center">
                    <svg className="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
                      <circle
                        className="opacity-25"
                        cx="12"
                        cy="12"
                        r="10"
                        stroke="currentColor"
                        strokeWidth="4"
                      />
                      <path
                        className="opacity-75"
                        fill="currentColor"
                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                      />
                    </svg>
                    Processing...
                  </span>
                ) : (
                  "Ask AI"
                )}
              </button>
            </form>
          </div>

          {/* Right Column - Answer Display */}
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
            <h2 className="text-xl font-semibold text-white mb-4">AI Response</h2>
            <div className="prose prose-invert">
              {answer ? (
                <div className="text-white/90 whitespace-pre-wrap">{answer}</div>
              ) : (
                <div className="text-white/50 italic">
                  Your AI response will appear here...
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
