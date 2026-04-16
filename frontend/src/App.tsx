import "./index.css";
import { useState } from "react";
import { uploadFile } from "./services/analysisService";
import api from "./services/api";

api
  .get("/")
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

function App() {
  const [file, setFile] = useState<File | null>(null);

  const handleUpload = async () => {
    if (!file) return;

    try {
      const res = await uploadFile(file);
      console.log("UPLOAD SUCCESS:", res);
    } catch (err) {
      console.error("UPLOAD ERROR:", err);
    }
  };

  return (
    <div>
      <h1>Upload Test</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <button
        onClick={handleUpload}
        type="button"
        className="text-body bg-neutral-secondary-medium box-border border border-default-medium hover:bg-neutral-tertiary-medium hover:text-heading focus:ring-4 focus:ring-neutral-tertiary shadow-xs font-medium leading-5 rounded-base text-sm px-4 py-2.5 focus:outline-none"
      >
        Upload
      </button>
    </div>
  );
}

export default App;
