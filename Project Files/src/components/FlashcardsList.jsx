import Flashcard from "./Flashcard";

function FlashcardsList({ cards }) {
  return (
    <div className="mt-10">

      <h2 className="text-3xl font-bold text-white mb-8">
        🃏 Flashcards
      </h2>

      <div className="grid md:grid-cols-2 gap-6">

        {cards.map((card, index) => (
          <Flashcard
            key={index}
            question={card.question}
            answer={card.answer}
          />
        ))}

      </div>

    </div>
  );
}

export default FlashcardsList;