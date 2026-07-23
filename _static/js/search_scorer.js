const _searchQuery = new URLSearchParams(window.location.search).get("q")?.toLowerCase().trim() || "";

window.Scorer = {
  score: result => {
    const [docName, title, anchor, descr, baseScore, filename] = result;
    let score = baseScore;

    // Demote release notes
    if (docName.startsWith("reference/release-notes/")) {
      return score - 20;
    }

    // Demote glossary
    if (docName === "reference/glossary") {
      return score - 20;
    }

    // Demote auto-generated command references (AMC, appliance, AAR)
    // When the query matches the command title, apply a smaller demotion
    // so they rank above release notes (-20) but below primary content
    if (docName.startsWith("reference/cmd-ref/")) {
      if (_searchQuery && title.toLowerCase().includes(_searchQuery)) {
        return score - 10;
      }
      return score - 20;
    }

    // Boost pages whose H1 title contains the search query
    if (anchor === "" && _searchQuery && title.toLowerCase().includes(_searchQuery)) score += 5;

    return score;
  },

  objNameMatch: 11,
  objPartialMatch: 6,
  objPrio: {0: 15, 1: 5, 2: -5},
  objPrioDefault: 0,
  title: 15,
  partialTitle: 7,
  term: 5,
  partialTerm: 2,
};
