# 🧠 Hydra Cluster Phase 1: Master Node Software Foundation

This repository contains the "Zero-Touch" automation logic and architectural foundation for **Node 1** of the Hydra AI Cluster. This node serves as the **Control Plane** (The Brain), responsible for resource orchestration, workload scheduling, and managing the distributed neural network tasks across the remaining three nodes.

---

## ## 🚀 Overview: What This Code Accomplishes

The `setup.sh` script is a professional-grade deployment tool designed to transform a standard Ubuntu 24.04 LTS headless installation into a hardened AI orchestration hub.

### 1. Automation (Zero-Touch Deployment)
Manual configuration of a Kubernetes environment involves over 50 complex commands and significant risk of human error. This script automates the entire pipeline—from repository injection to firewall hardening—ensuring a consistent "Source of Truth" for your cluster's OS.

### 2. Containerization (Docker Engine)
Docker provides the "Standard Unit of Software" for AI. By utilizing Docker:
* **Isolation:** AI models (like Llama 3 or Stable Diffusion) run in isolated environments, preventing library conflicts.
* **Portability:** You can pull pre-baked AI images from Hugging Face or Docker Hub and run them instantly without manual Python environment setup.

### 3. Orchestration (K3s Lightweight Kubernetes)
K3s is a highly optimized, CNCF-certified Kubernetes distribution. In this 4-node project, K3s acts as the cluster's operating system:
* **Self-Healing:** If a worker node fails, K3s automatically redistributes the AI inference task to a healthy node.
* **Scalability:** It treats all 4 CPUs and all future GPUs as a single pool of resources.

### 4. GPU Future-Proofing (NVIDIA Container Toolkit)
While the initial setup uses an NVIDIA GT 210, this script installs the modern **NVIDIA Container Toolkit**. This creates a software "bridge" that allows Docker and K3s to communicate with GPU hardware. When you upgrade to a modern RTX card, the cluster will recognize the CUDA cores immediately without needing a software rebuild.

---

## 🛠️ Detailed Step-by-Step Setup Guide

### Phase A: Hardware & OS Prep
1. Install **Ubuntu Server 24.04 LTS** (64-bit) on your AMD Ryzen 3 4100 system.
2. Ensure the system is connected via **Ethernet** (WiFi is not recommended for cluster stability).
3. Identify the local IP address of the machine via your router or by typing `hostname -I`.

### Phase B: Remote Deployment
From your main workstation/laptop, perform the following:


# ⚡ Hydra Cluster: Distributed Control & Power Management

This section explains how the **Hydra Control Engine** manages the 4-node Ryzen 3 cluster to maximize computational throughput.

## ## How It Controls Every Node
The controller uses **Kubernetes Node Selectors**. Instead of manually logging into each server, the Python script sends a "Manifest" to the Master Node (Node 1). This manifest contains a `nodeSelector` tag. 
* **Node 1 (The Brain):** Reserves its 4 cores for scheduling, API handling, and traffic routing.
* **Nodes 2, 3, 4 (The Muscle):** These nodes wait for "Pod" assignments. When the Python controller identifies a heavy AI task, it pushes the workload to these nodes via the K3s API.

## ## Power Utilization Strategy
To ensure the cluster doesn't overheat or waste electricity, the software follows these power rules:

1. **Dynamic Scaling:** If no AI tasks are in the queue, the worker nodes stay in "Idle" mode, consuming minimal wattage.
2. **Parallel Processing:** For massive datasets, the controller splits the data into 3 chunks and sends one to each worker node. This allows the cluster to use all **16 CPU cores** simultaneously.
3. **GPU Passthrough:** When an NVIDIA GPU is detected on any node, the controller prioritizes that node for `cuda` tasks, significantly reducing the time the CPU spends at 100% load.

---

## 🔍 Troubleshooting the Controller

### 1. "Connection Refused" to localhost:8080
* **Cause:** The Python script cannot find the K3s configuration file.
* **Fix:** Ensure your user has access to the K3s config. Run: 
  `export KUBECONFIG=/etc/rancher/k3s/k3s.yaml` 
  or run the script with `sudo`.

### 2. Task Stays in "Pending" State
* **Cause:** The controller sent a task to a node that doesn't have enough RAM or is offline.
* **Fix:** Check node resources with `kubectl describe node <node-name>`. Ensure `swap` is disabled on all nodes as per Phase 1 instructions.

### 3. Subprocess Errors
* **Cause:** The script tries to run `kubectl` but it isn't in the system path.
* **Fix:** Verify K3s is installed correctly by running `which kubectl`. If it returns nothing, the Phase 1 `setup.sh` did not complete successfully.

---

## 📈 Next Step: Deployment
With the **Setup Script** (Body), the **AI Core** (Mind), and the **Controller** (Nervous System) ready, your 4-node Ryzen 3 Hydra is officially ready for the Blueprint submission.
