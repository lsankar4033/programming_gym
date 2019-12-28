pub mod graph {
    use graph_items::edge::Edge;
    use graph_items::node::Node;
    use std::collections::HashMap;

    pub struct Graph {
        pub nodes: Vec<Node>,
        pub edges: Vec<Edge>,
        pub attrs: HashMap<String, String>,
    }

    impl Graph {
        pub fn new() -> Self {
            Graph {
                nodes: Vec::new(),
                edges: Vec::new(),
                attrs: HashMap::new(),
            }
        }

        pub fn with_nodes(mut self, nodes: &[Node]) -> Self {
            self.nodes = nodes.to_vec();
            self
        }

        pub fn with_edges(mut self, edges: &[Edge]) -> Self {
            self.edges = edges.to_vec();
            self
        }

        pub fn with_attrs(mut self, attrs: &[(&str, &str)]) -> Self {
            for attr in attrs.iter() {
                self.attrs.insert(attr.0.to_string(), attr.1.to_string());
            }

            self
        }

        pub fn get_node(&self, label: &str) -> Option<&Node> {
            self.nodes.iter().find(|&n| n.label == label.to_string())
        }
    }

    pub mod graph_items {

        pub mod edge {
            use std::collections::HashMap;

            #[derive(Clone, PartialEq, Debug)]
            pub struct Edge {
                from: String,
                to: String,
                attrs: HashMap<String, String>,
            }

            impl Edge {
                pub fn new(f: &str, t: &str) -> Self {
                    Edge {
                        from: f.to_string(),
                        to: t.to_string(),
                        attrs: HashMap::new(),
                    }
                }

                pub fn with_attrs(mut self, attrs: &[(&str, &str)]) -> Self {
                    for attr in attrs.iter() {
                        self.attrs.insert(attr.0.to_string(), attr.1.to_string());
                    }

                    self
                }
            }
        }

        pub mod node {
            use std::collections::HashMap;

            #[derive(Clone, PartialEq, Debug)]
            pub struct Node {
                pub label: String,
                attrs: HashMap<String, String>,
            }

            impl Node {
                pub fn new(s: &str) -> Self {
                    Node {
                        label: s.to_string(),
                        attrs: HashMap::new(),
                    }
                }

                pub fn with_attrs(mut self, attrs: &[(&str, &str)]) -> Self {
                    for attr in attrs.iter() {
                        self.attrs.insert(attr.0.to_string(), attr.1.to_string());
                    }

                    self
                }

                pub fn get_attr(&self, key: &str) -> Option<&str> {
                    if let Some(v) = self.attrs.get(key) {
                        Some(v)
                    } else {
                        None
                    }
                }
            }
        }
    }
}
