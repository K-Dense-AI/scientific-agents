# AGENTS.md: Crop Specific Guidance Future Expansion Profile

This branch is future-only. It explains how to route crop-specific questions and how future crop profiles should be designed, but it does not implement maize, corn, wheat, rice, soybean, sorghum, cotton, forage, vegetable, orchard, vineyard, or other crop recommendations.

## Source Basis

Task 8 SRC-081 through SRC-090, identifying land-grant crop portals and crop-guide routing sources. Detailed URLs stay in the Task 8 map, and no crop subdirectories or filled crop profiles are created in this branch.

## When To Use

- A task asks whether crop-specific agronomist guidance should exist, how future crop profiles should be organized, or how to keep current advice conservative until crop profiles are added.
- A current crop question needs routing to the root agronomist profile plus an existing task profile rather than a filled crop handbook.

## Inputs To Request

- For current routing: crop, region, production system, growth stage, planting date, hybrid or variety, maturity group, soil test method, soil texture, drainage, previous crop, residue, irrigation or rainfall, scouting, nutrient program, harvest goal, market class, and deadline.
- For future profile design: production regions, decisions that differ from general agronomy, local calibration sources, phenology stages, common failure modes, quality standards, machinery needs, pest risk, fertility and water timing, and economic decision points.

## Outputs To Produce

- Future expansion guidance, scoping notes, conservative routing advice, criteria for whether a crop profile is warranted, an unfilled outline, warnings that the branch has no crop profile, and local data needed before crop advice could be confident.

## Decision Rules

- Route current crop questions to the root agronomist profile plus the relevant existing task profile, such as establishment, fertility, water, pest integration, climate, economics, or extension writing.
- A future crop profile is justified only when repeated decisions in that crop need phenology, planting, fertility, water, pest, harvest quality, storage, market, and economics detail beyond general agronomy.
- Any future crop profile must use current local crop guides, trials, IPM references, nutrient references, labels, and extension sources.
- Every crop-specific numeric rate, date, threshold, crop coefficient, variety result, planting window, or budget must be marked local to crop, region, season, and source year.
- Do not add crop prescription tables, crop recipes, universal variety winners, or transplant regional crop guides across agroecologies.
- Do not create crop subdirectories or filled crop AGENTS.md files in this task.
- Reject placeholders that look complete but lack source grounding, local calibration, and referral boundaries.

## Boundaries

This branch does not implement individual crop profiles. Use `crop-scientist` for physiology, phenology, and yield formation science. Use crop protection, weed, fertility, water, breeding, precision, economics, or extension profiles when those are the main current decision.

## Local Caveats And Source Guardrails

Crop-specific recommendations are especially local. Current advice must state uncertainty and name the local extension, label, regulator, crop guide, trial, or certified adviser source that should override general guidance. Do not use unsupported sources, vendor marketing, SEO pages, anonymous advice, AI summaries, dealer plots, testimonials, or placeholders as agronomic authority. Keep detailed citations in the Task 8 source map rather than bloating this profile with URLs.
