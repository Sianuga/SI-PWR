# University AI Projects Repository

This repository contains a collection of university projects developed for an Artificial Intelligence course, covering a variety of topics:

- **Path Finding Algorithms**
- **Halma Game - Minimax Algorithm**
- **Dishwasher Representation (Expert System)**
- **Machine Learning Analysis**
- **Multi-Layer Perceptron Training**

---

## 1. Path Finding Algorithms

**Project Overview:**  
Provide an end-to-end solution for transit route planning and optimization. The system reads CSV data to construct a transit network, then employs multiple routing algorithms to find optimal paths between stops. It uses a graph-based model to represent transit stops and connections, with classical algorithms (Dijkstra’s, A*) and metaheuristic methods (Tabu Search) to address complex multi-stop scenarios.

**Key Features:**  
- **Multi-Criteria Optimization:** Users can choose between time-based optimization, path (transfer) minimization, and other criteria.
- **Multiple Routing Algorithms:** Implements Dijkstra’s algorithm for time optimization, A* search with geographic heuristics, and various Tabu Search strategies.
- **Graph Data Management:** Reads CSV files to build a detailed graph with nodes for stops and edges for connections (including departure/arrival times and transit lines).
- **Performance Tracking:** Each route search prints execution times, enabling benchmarking of algorithm efficiency.

---

## 2. Halma Game - Minimax Algorithm

**Project Overview:**  
Implements the classic board game Halma using a minimax algorithm enhanced with alpha-beta pruning to optimize decision-making. The project simulates game states, evaluates moves using multiple heuristic strategies, and determines the best move for each turn. It demonstrates the application of search and evaluation techniques in a competitive two-player game.

**Key Features:**  
- **Minimax with Alpha-Beta Pruning:** Efficiently searches for optimal moves by reducing the number of evaluated nodes.
- **Heuristic Evaluation:** Utilizes several strategies (e.g., distance-to-goal, center control, formation) to evaluate board states.
- **Dynamic Move Generation:** Generates possible moves, including jump moves, to reflect realistic game scenarios.
- **Game Simulation:** Provides a complete game loop with move logging, round tracking, and outcome determination.

---

## 3. Dishwasher Representation (Expert System)

**Project Overview:**  
Develops an expert system to simulate dishwasher operation using a rule-based approach. The system represents physical components, required items, and adjustable settings of a dishwasher, and applies rules to determine if the dishwasher can operate correctly or if issues are present. It demonstrates the use of the `experta` library for constructing a knowledge-based diagnostic system.

**Key Features:**  
- **Knowledge Representation:** Models dishwasher components, required items, and settings as facts.
- **Rule-Based Reasoning:** Applies rules to diagnose common issues (e.g., missing items, improper settings) and to suggest corrective actions.
- **Scenario Handling:** Addresses multiple scenarios, such as proper operation, missing ingredients, and specific operational problems (e.g., dishes not drying, water not draining).
- **Diagnostic Output:** Provides detailed feedback on detected issues and recommended solutions.

---

## 4. Machine Learning Analysis

**Project Overview:**  
Conducts a comprehensive data analysis and classification study on a real-world dataset. The project performs extensive preprocessing (normalization, standardization, PCA, and imputation), followed by training and evaluating multiple classifiers. It also visualizes data distributions and classifier performance metrics, showcasing practical applications of machine learning techniques.

**Key Features:**  
- **Data Preprocessing:** Implements normalization, standardization, PCA, and missing value imputation to prepare the dataset.
- **Classifier Evaluation:** Trains several classifiers (Naive Bayes, Decision Trees, Random Forest, SVM) and compares their performance using classification reports.
- **Visualization:** Generates plots for data distributions and a heatmap to compare classifier accuracies across different preprocessing methods.
- **Comprehensive Analysis:** Provides insights into the impact of various data preparation techniques on model performance.

---

## 5. Multi-Layer Perceptron Training

**Project Overview:**  
Focuses on training a multi-layer perceptron (MLP) regressor for prediction tasks using a dataset enriched with both FastText and BERT embeddings. The project explores different learning rates, model sizes, and regularization parameters, tracking training loss to optimize performance. It demonstrates neural network training and hyperparameter tuning in a practical scenario.

**Key Features:**  
- **Hybrid Embedding Approach:** Combines FastText and BERT embeddings to create robust feature representations.
- **Neural Network Training:** Trains an MLP regressor to predict target variables, such as a funniness score.
- **Hyperparameter Tuning:** Experiments with various learning rates, model sizes (number of neurons), and regularization parameters.
- **Loss Curve Visualization:** Plots training loss curves to illustrate model convergence and the effects of different hyperparameter settings.
