function UploadCard({ handleFileUpload, filename }) {
  return (
    <div className="bg-slate-800 border-2 border-dashed border-slate-600 rounded-2xl p-10 text-center hover:border-blue-500 transition">

      <div className="text-6xl mb-4">📂</div>

      <h2 className="text-3xl font-bold text-white">
        Upload your Notes
      </h2>

      <p className="text-slate-400 mt-3 mb-8">
        Supports PDF and DOCX files
      </p>

      <input
        id="file-upload"
        type="file"
        accept=".pdf,.docx"
        className="hidden"
        onChange={handleFileUpload}
      />

      <label
        htmlFor="file-upload"
        className="
          inline-block
          bg-blue-600
          hover:bg-blue-700
          text-white
          px-8
          py-4
          rounded-xl
          cursor-pointer
          transition
          font-semibold
        "
      >
        Choose File
      </label>

      {filename && (
        <div className="mt-8 bg-green-900/30 border border-green-600 rounded-xl p-4">

          <p className="text-green-400 font-semibold">
            ✓ Uploaded Successfully
          </p>

          <p className="text-white mt-2 break-all">
            {filename}
          </p>

        </div>
      )}

    </div>
  );
}

export default UploadCard;