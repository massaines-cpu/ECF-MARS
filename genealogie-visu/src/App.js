import { useState } from "react";

const people = {
  1: { prenom: "Blaža", nom: "Lahblah", naissance: null, deces: null },
  2: { prenom: "Marie Chantal", nom: "Lahblah-Lowblow", naissance: "1903", deces: "2012" },
  3: { prenom: "Jean-Chrysostome", nom: "de Taxi du Poet", naissance: "1911", deces: null },
  4: { prenom: "Eude-Edmon", nom: "Lowblow", naissance: "1930", deces: null },
  5: { prenom: "Eugénie", nom: "Lowblow", naissance: "1940", deces: null },
  6: { prenom: "X", nom: "Lowblow-Lahblah de Taxi du Poet", naissance: "1966", deces: null },
  7: { prenom: "Fanny", nom: "Lowblow", naissance: "1920", deces: "1987" },
  8: { prenom: "River Willow Moonbeam", nom: "Lahblah", naissance: "1968", deces: null },
  9: { prenom: "Zephyr Rainbow Sunshine", nom: "Lahblah", naissance: "1969", deces: null },
  10: { prenom: "Belinda Starflower", nom: "Lahblah", naissance: "1970", deces: null },
  11: { prenom: "Orion Skydancer Phoenix", nom: "Lahblah", naissance: "1972", deces: null },
  12: { prenom: "Juniper Sage Harmony", nom: "Lahblah", naissance: "1973", deces: "2004" },
};

const bioRelations = [
  { parent: 2, enfant: 4 }, { parent: 2, enfant: 5 },
  { parent: 3, enfant: 6 }, { parent: 4, enfant: 6 }, { parent: 4, enfant: 7 },
  { parent: 5, enfant: 2 }, { parent: 5, enfant: 6 },
  { parent: 10, enfant: 1 }, { parent: 11, enfant: 2 },
];

const adoptiveRelations = [
  { parent: 2, enfant: 8 }, { parent: 2, enfant: 9 },
  { parent: 2, enfant: 10 }, { parent: 2, enfant: 11 },
  { parent: 2, enfant: 12 }, { parent: 3, enfant: 5 },
  { parent: 8, enfant: 1 }, { parent: 9, enfant: 1 },
];

const generations = [
  [2, 3],
  [4, 5],
  [6, 7, 8, 9, 10, 11, 12],
  [1],
];

const CARD_W = 160;
const CARD_H = 70;
const H_GAP = 30;
const V_GAP = 100;

function getPositions() {
  const pos = {};
  generations.forEach((gen, gi) => {
    const totalW = gen.length * CARD_W + (gen.length - 1) * H_GAP;
    const startX = -totalW / 2;
    gen.forEach((id, i) => {
      pos[id] = {
        x: startX + i * (CARD_W + H_GAP),
        y: gi * (CARD_H + V_GAP),
      };
    });
  });
  return pos;
}

export default function App() {
  const [selected, setSelected] = useState(null);
  const pos = getPositions();

  const totalH = generations.length * (CARD_H + V_GAP);
  const allX = Object.values(pos).map(p => p.x);
  const minX = Math.min(...allX) - 20;
  const maxX = Math.max(...allX) + CARD_W + 20;
  const svgW = maxX - minX;
  const svgH = totalH + 20;

  const allRelations = [
    ...bioRelations.map(r => ({ ...r, type: "bio" })),
    ...adoptiveRelations.map(r => ({ ...r, type: "adoptif" })),
  ];

  const getParents = (id) => [
    ...bioRelations.filter(r => r.enfant === id).map(r => ({ id: r.parent, type: "bio" })),
    ...adoptiveRelations.filter(r => r.enfant === id).map(r => ({ id: r.parent, type: "adoptif" })),
  ];
  const getChildren = (id) => [
    ...bioRelations.filter(r => r.parent === id).map(r => ({ id: r.enfant, type: "bio" })),
    ...adoptiveRelations.filter(r => r.parent === id).map(r => ({ id: r.enfant, type: "adoptif" })),
  ];

  return (
    <div style={{ background: "#faf8f4", minHeight: "100vh", padding: "30px", fontFamily: "Georgia, serif" }}>
      <h1 style={{ textAlign: "center", fontSize: "22px", color: "#2c2c2c", fontWeight: "normal", letterSpacing: "2px", marginBottom: "10px", borderBottom: "1px solid #ccc", paddingBottom: "10px" }}>
        L'étrange généalogie
      </h1>
      <p style={{ textAlign: "center", fontSize: "11px", color: "#999", marginBottom: "30px" }}>
        appuie pour voir les relations — <span style={{ color: "#555", borderBottom: "1px solid #555" }}>ligne continue</span> = biologique &nbsp;|&nbsp; <span style={{ color: "#555", borderBottom: "1px dashed #555" }}>pointillé</span> = adoptif
      </p>

      <div style={{ overflowX: "auto" }}>
        <svg width={svgW} height={svgH} style={{ display: "block", margin: "0 auto" }}>
          {/* Lignes de relations */}
          {allRelations.map((r, i) => {
            const p = pos[r.parent];
            const c = pos[r.enfant];
            if (!p || !c) return null;
            const x1 = p.x - minX + CARD_W / 2;
            const y1 = p.y + CARD_H;
            const x2 = c.x - minX + CARD_W / 2;
            const y2 = c.y;
            const my = (y1 + y2) / 2;
            const isHighlighted = selected && (r.parent === selected || r.enfant === selected);
            return (
              <path
                key={i}
                d={`M${x1},${y1} C${x1},${my} ${x2},${my} ${x2},${y2}`}
                fill="none"
                stroke={isHighlighted ? "#8b4513" : "#bbb"}
                strokeWidth={isHighlighted ? 2 : 1}
                strokeDasharray={r.type === "adoptif" ? "5,4" : "none"}
              />
            );
          })}

          {/* Cartes des individus */}
          {Object.entries(pos).map(([id, p]) => {
            const person = people[parseInt(id)];
            const isSelected = selected === parseInt(id);
            const isDead = !!person.deces;
            const cx = p.x - minX;
            const cy = p.y;
            return (
              <g key={id} onClick={() => setSelected(isSelected ? null : parseInt(id))} style={{ cursor: "pointer" }}>
                <rect
                  x={cx} y={cy}
                  width={CARD_W} height={CARD_H}
                  rx={4}
                  fill={isDead ? "#ece8e0" : "#fff"}
                  stroke={isSelected ? "#8b4513" : "#bbb"}
                  strokeWidth={isSelected ? 2 : 1}
                />
                <text x={cx + CARD_W / 2} y={cy + 22} textAnchor="middle" fontSize="11" fontWeight="bold" fill="#2c2c2c" fontFamily="Georgia, serif">
                  {person.prenom}
                </text>
                <text x={cx + CARD_W / 2} y={cy + 36} textAnchor="middle" fontSize="10" fill="#666" fontStyle="italic" fontFamily="Georgia, serif">
                  {person.nom}
                </text>
                <text x={cx + CARD_W / 2} y={cy + 52} textAnchor="middle" fontSize="9" fill="#999" fontFamily="Georgia, serif">
                  {person.naissance || "?"}{person.deces ? ` — ${person.deces}` : ""}
                </text>
                {isDead && (
                  <text x={cx + CARD_W - 10} y={cy + 14} textAnchor="middle" fontSize="10" fill="#999">✝</text>
                )}
              </g>
            );
          })}
        </svg>
      </div>

      {/* Panneau de détail */}
      {selected && (
        <div style={{ position: "fixed", bottom: "20px", right: "20px", background: "#fff", border: "1px solid #bbb", borderRadius: "6px", padding: "16px", minWidth: "240px", maxWidth: "300px", boxShadow: "0 4px 16px rgba(0,0,0,0.1)", fontFamily: "Georgia, serif" }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "12px" }}>
            <div>
              <div style={{ fontSize: "14px", fontWeight: "bold", color: "#2c2c2c" }}>{people[selected].prenom}</div>
              <div style={{ fontSize: "11px", color: "#666", fontStyle: "italic" }}>{people[selected].nom}</div>
              <div style={{ fontSize: "10px", color: "#999", marginTop: "2px" }}>
                {people[selected].naissance || "?"}{people[selected].deces ? ` — ${people[selected].deces}` : " — vivant(e)"}
              </div>
            </div>
            <button onClick={() => setSelected(null)} style={{ background: "none", border: "none", cursor: "pointer", fontSize: "16px", color: "#999" }}>×</button>
          </div>
          <div style={{ marginBottom: "10px" }}>
            <div style={{ fontSize: "10px", color: "#999", textTransform: "uppercase", letterSpacing: "1px", marginBottom: "4px" }}>Parents</div>
            {getParents(selected).length === 0
              ? <div style={{ fontSize: "11px", color: "#bbb" }}>Aucun parent connu</div>
              : getParents(selected).map(({ id, type }) => (
                <div key={id} style={{ fontSize: "11px", color: "#444", marginBottom: "2px" }}>
                  {people[id].prenom} {people[id].nom}
                  <span style={{ fontSize: "9px", color: type === "bio" ? "#4a7c4a" : "#a0703a", marginLeft: "4px" }}>({type})</span>
                </div>
              ))}
          </div>
          <div>
            <div style={{ fontSize: "10px", color: "#999", textTransform: "uppercase", letterSpacing: "1px", marginBottom: "4px" }}>Enfants</div>
            {getChildren(selected).length === 0
              ? <div style={{ fontSize: "11px", color: "#bbb" }}>Aucun enfant</div>
              : getChildren(selected).map(({ id, type }) => (
                <div key={id} style={{ fontSize: "11px", color: "#444", marginBottom: "2px" }}>
                  {people[id].prenom} {people[id].nom}
                  <span style={{ fontSize: "9px", color: type === "bio" ? "#4a7c4a" : "#a0703a", marginLeft: "4px" }}>({type})</span>
                </div>
              ))}
          </div>
        </div>
      )}
    </div>
  );
}