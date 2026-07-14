import { useState } from "react";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import TextInput from "../components/TextInput";
import SummaryCard from "../components/SummaryCard";
import FlashcardsList from "../components/FlashcardsList";
import ScheduleCard from "../components/ScheduleCard";
import Button from "../components/Button";
import Footer from "../components/Footer";
import UploadCard from "../components/UploadCard";
import toast from "react-hot-toast";
import Loader from "../components/Loader";
import { getCorrectQuizOption, isQuizOptionCorrect } from "../utils/quizUtils";

import {
  uploadMaterial,
  generateSummary,
  generateFlashcards,
  generateSchedule,
  generateQuiz,
} from "../services/api";

function Home() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [flashcards, setFlashcards] = useState([]);
  const [schedule, setSchedule] = useState("");
  const [quiz, setQuiz] = useState([]);
  const [quizResponses, setQuizResponses] = useState([]);
  const [quizCompleted, setQuizCompleted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [filename, setFilename] = useState("");

  // Upload PDF/DOCX
  const handleFileUpload = async (event) => {
    const file = event.target.files[0];

    if (!file) return;

    try {
      const response = await uploadMaterial(file);

      setText(response.data.text);
      setFilename(response.data.filename);

      toast.success("File uploaded successfully!");
    } catch (error) {
      console.error(error);
      toast.error("Upload failed.");
    }
  };

  const clearOtherResults = (currentSection) => {
    if (currentSection !== "summary") setSummary("");
    if (currentSection !== "flashcards") setFlashcards([]);
    if (currentSection !== "schedule") setSchedule("");
    if (currentSection !== "quiz") {
      setQuiz([]);
      setQuizResponses([]);
      setQuizCompleted(false);
    }
  };

  // Generate Summary
  const handleGenerateSummary = async () => {
    if (!text.trim()) {
      alert("Please enter some study material.");
      return;
    }

    try {
      setLoading(true);
      clearOtherResults("summary");

      const response = await generateSummary(text);

      setSummary(response.data.summary);

      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth",
      });

    } catch (error) {
      console.error(error);
      toast.error("Failed to generate summary.");
    } finally {
      setLoading(false);
    }
  };

  // Generate Flashcards
  const handleGenerateFlashcards = async () => {
    if (!text.trim()) {
      toast.error("Please enter some study material.");
      return;
    }

    try {
      setLoading(true);
      clearOtherResults("flashcards");

      const response = await generateFlashcards(text);

      setFlashcards(response.data.flashcards);

      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth",
      });

    } catch (error) {
      console.error(error);
      alert("Failed to generate flashcards.");
    } finally {
      setLoading(false);
    }
  };

  // Generate Schedule
  const handleGenerateSchedule = async () => {
    if (!text.trim()) {
      alert("Please enter some study material.");
      return;
    }

    try {
      setLoading(true);
      clearOtherResults("schedule");

      const response = await generateSchedule(text);

      setSchedule(response.data.schedule);

      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth",
      });

    } catch (error) {
      console.error(error);
      alert("Failed to generate schedule.");
    } finally {
      setLoading(false);
    }
  };

  // Generate Quiz
  const handleGenerateQuiz = async () => {
    if (!text.trim()) {
      toast.error("Please enter some study material.");
      return;
    }

    try {
      setLoading(true);
      clearOtherResults("quiz");

      const response = await generateQuiz(text);

      setQuiz(response.data.quiz || []);
      setQuizResponses([]);
      setQuizCompleted(false);

      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth",
      });

    } catch (error) {
      console.error(error);
      toast.error("Failed to generate quiz.");
    } finally {
      setLoading(false);
    }
  };

  const handleSelectQuizOption = (questionIndex, selectedOption) => {
    setQuizResponses((prev) => {
      const next = [...prev];
      next[questionIndex] = { answered: true, selectedOption };
      const allAnswered = next.slice(0, quiz.length).every((response) => response?.answered);
      if (allAnswered) {
        setQuizCompleted(true);
      }
      return next;
    });
  };

  const quizScore = quiz.reduce((score, question, index) => {
    const response = quizResponses[index];
    const correctOption = getCorrectQuizOption(question);
    return score + (response?.answered && isQuizOptionCorrect(response.selectedOption, correctOption) ? 1 : 0);
  }, 0);

  return (
    <>
      <Navbar />

      {loading && <Loader />}

      <Hero />

      <div className="max-w-6xl mx-auto px-6 py-10">

        {/* Feature Cards */}

        {/* Upload Card */}

        <UploadCard
          handleFileUpload={handleFileUpload}
          filename={filename}
        />

        {/* Text Area */}
        <div className="bg-slate-800 border border-slate-700 rounded-2xl shadow-xl p-8 mb-8">

          <h2 className="text-2xl font-bold text-white mb-4">
            📝 Study Material
          </h2>

          <TextInput
            value={text}
            onChange={(e) => setText(e.target.value)}
          />

        </div>

        {/* Buttons */}
        <div className="flex flex-wrap justify-center gap-5 mb-10">

          <Button
            title="📄 Generate Summary"
            loading={loading}
            onClick={handleGenerateSummary}
          />

          <Button
            title="🃏 Generate Flashcards"
            loading={loading}
            onClick={handleGenerateFlashcards}
          />

          <Button
            title="📅 Generate Schedule"
            loading={loading}
            onClick={handleGenerateSchedule}
          />

          <Button
            title="🧠 Generate Quiz"
            loading={loading}
            onClick={handleGenerateQuiz}
          />

        </div>

        {/* Results */}

        {summary && (
          <SummaryCard summary={summary} />
        )}

        {flashcards.length > 0 && (
          <FlashcardsList cards={flashcards} />
        )}

        {schedule && (
          <ScheduleCard schedule={schedule} />
        )}

        {quiz.length > 0 && (
          <div className="bg-slate-800 border border-slate-700 rounded-2xl shadow-xl p-8 mb-8">
            <h2 className="text-2xl font-bold text-white mb-6">
              🧠 Quiz
            </h2>

            {quiz.map((question, index) => {
              const response = quizResponses[index];

              return (
                <div key={`${question.question}-${index}`} className="mb-6 p-6 rounded-xl bg-slate-900 border border-slate-700">
                  <p className="text-white font-semibold mb-4">
                    {index + 1}. {question.question}
                  </p>

                  <div className="grid gap-3">
                    {question.options.map((option) => {
                      const correctOption = getCorrectQuizOption(question);
                      const isSelected = isQuizOptionCorrect(response?.selectedOption, option);
                      const isCorrect = isQuizOptionCorrect(option, correctOption);
                      let optionClass = "w-full text-left px-4 py-3 rounded-lg border transition-all";

                      if (response?.answered) {
                        if (isSelected && isCorrect) {
                          optionClass += " bg-green-600 border-green-500 text-white";
                        } else if (isSelected && !isCorrect) {
                          optionClass += " bg-red-600 border-red-500 text-white";
                        } else if (isCorrect) {
                          optionClass += " bg-green-100 text-green-900 border-green-400";
                        } else {
                          optionClass += " bg-slate-800 border-slate-600 text-slate-300";
                        }
                      } else {
                        optionClass += " bg-slate-800 border-slate-600 text-slate-200 hover:bg-slate-700";
                      }

                      return (
                        <button
                          key={`${question.question}-${option}`}
                          type="button"
                          className={optionClass}
                          onClick={() => handleSelectQuizOption(index, option)}
                          disabled={Boolean(response?.answered)}
                        >
                          {option}
                        </button>
                      );
                    })}
                  </div>
                </div>
              );
            })}

            {quizCompleted && (
              <div className="mt-6 rounded-xl border border-emerald-500 bg-emerald-950/70 p-6">
                <h3 className="text-xl font-bold text-white mb-2">
                  📊 Quiz Scorecard
                </h3>
                <p className="text-emerald-200 text-lg font-semibold">
                  You got {quizScore} out of {quiz.length} correct.
                </p>
                <p className="text-emerald-200 mt-2">
                  Accuracy: {quiz.length > 0 ? Math.round((quizScore / quiz.length) * 100) : 0}%
                </p>
                <p className="text-emerald-100 mt-3">
                  Great work! Review the questions you missed and try again to improve your score.
                </p>
              </div>
            )}
          </div>
        )}

      </div>

      <Footer />
    </>
  );
}

export default Home;