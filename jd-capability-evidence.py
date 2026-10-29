#!/usr/bin/env python3
"""Reproduce the JD-visibility statistics used by the Agent Capability Atlas.

The metric is corpus visibility: whether a term family occurs anywhere in a JD.
It is NOT a count of mandatory requirements, core responsibilities, or market share.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ADJACENT_ONLY = {
    19: "AI product / application leadership",
    24: "Agentic RL research and training infrastructure",
    25: "General LLM training and serving systems",
}

TERMS = {
    "evaluation": {
        "label": "评测 / 评估（广义）",
        "pattern": r"评测|评估|Eval|Benchmark|AgentBench|GAIA",
        "basis": "broad: includes evaluation responsibilities, requirements, preferences, and collaboration",
    },
    "multi_agent": {
        "label": "Multi-Agent",
        "pattern": r"Multi-Agent|多智能体|多 Agent|多Agent|MAS",
        "basis": "literal term family",
    },
    "tool_use": {
        "label": "Tool Use / 工具调用",
        "pattern": r"Tool|工具调用|Function Call|function calling|Tool-Use|Tool Use",
        "basis": "broad: Tool can include platform and integration contexts",
    },
    "orchestration": {
        "label": "编排 / 调度 / 工作流",
        "pattern": r"调度|编排|工作流|Orchestrat",
        "basis": "broad: combines workflow, task orchestration, and resource scheduling",
    },
    "frameworks": {
        "label": "Agent 框架",
        "pattern": r"LangChain|LangGraph|Langchain|CrewAI|AutoGen|AgentScope|Dify|ADK|Spring AI|LlamaIndex|OpenAI Agent|Agent 框架|Agent框架",
        "basis": "literal framework family",
    },
    "observability": {
        "label": "可观测 / Trace",
        "pattern": r"可观测|Trace|trace|Telemetry|监控|OpenTelemetry|观测",
        "basis": "broad: includes monitoring and trajectory tracing",
    },
    "rag": {
        "label": "RAG / 知识库",
        "pattern": r"RAG|知识库|检索增强|知识引擎",
        "basis": "literal term family",
    },
    "execution_environment": {
        "label": "执行环境（广义）",
        "pattern": r"Runtime|沙箱|Sandbox|sandbox|Firecracker|gVisor|Kata|Wasm|虚拟化|容器",
        "basis": "broad: runtime, sandbox, virtualization, and containers are not interchangeable",
    },
    "memory": {
        "label": "Memory / 记忆",
        "pattern": r"Memory|记忆",
        "basis": "literal term family",
    },
    "long_task": {
        "label": "长任务 / 恢复",
        "pattern": r"长任务|长程|Checkpoint|状态持久化|失败重试|恢复",
        "basis": "broad: combines task duration, persistence, retry, and recovery",
    },
    "context": {
        "label": "Context Engineering",
        "pattern": r"上下文工程|Context Engineering|上下文管理|上下文压缩",
        "basis": "literal term family",
    },
    "skills": {
        "label": "Skills",
        "pattern": r"Skill|Skills",
        "basis": "literal term family; case-sensitive by design",
    },
    "ai_coding": {
        "label": "AI Coding / AI-native SDLC",
        "pattern": r"AI Coding|Spec Coding|AI 辅助研发|AI Native|vibe coding|Vibe",
        "basis": "literal term family",
    },
    "mcp_a2a": {
        "label": "MCP / A2A（字面）",
        "pattern": r"MCP|A2A",
        "basis": "literal only; generic protocol-layer language is excluded",
    },
    "multimodal": {
        "label": "多模态 / 语音 / 视觉",
        "pattern": r"多模态|语音|视觉交互",
        "basis": "literal term family",
    },
    "post_training": {
        "label": "后训练 / RL",
        "pattern": r"强化学习|RL|后训练|Post-Train|SFT|DPO|GRPO",
        "basis": "broad: includes research, engineering, and preferred-experience contexts",
    },
    "inference": {
        "label": "推理性能 / 成本（广义）",
        "pattern": r"推理优化|推理成本|延迟|vLLM|vllm|时延",
        "basis": "broad: latency can refer to application rather than model serving",
    },
    "harness": {
        "label": "Harness（字面）",
        "pattern": r"Harness|harness",
        "basis": "literal only; no density ranking because JD length and bilingual duplication vary",
    },
    "kubernetes": {
        "label": "Kubernetes（字面）",
        "pattern": r"Kubernetes",
        "basis": "literal only",
    },
    "microservices": {
        "label": "微服务（字面）",
        "pattern": r"微服务",
        "basis": "literal only",
    },
    "middleware": {
        "label": "中间件（字面）",
        "pattern": r"中间件",
        "basis": "literal only",
    },
}


def parse_jobs(text):
    matches = list(re.finditer(r"^### (\d+)\. (.+)$", text, re.M))
    jobs = {}
    for index, match in enumerate(matches):
        job_id = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end]
        # A group heading belongs to the corpus, not to the preceding job.
        lines = [line for line in block.splitlines() if not line.startswith("## ")]
        jobs[job_id] = {"title": match.group(2).strip(), "text": "\n".join(lines)}
    return jobs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jd_file", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    raw = args.jd_file.read_bytes()
    text = raw.decode("utf-8")
    jobs = parse_jobs(text)
    if len(jobs) != 25:
        raise ValueError(f"Expected 25 JDs in this corpus, found {len(jobs)}")
    core_ids = sorted(set(jobs) - set(ADJACENT_ONLY))
    result = {
        "method": {
            "metric": "JD visibility, not mandatory-requirement frequency",
            "segmentation": "Remove group headings before matching; one count per job per term family",
            "core_corpus": "22 jobs; excludes #19, #24, #25 for sensitivity analysis only",
            "adjacent_only": ADJACENT_ONLY,
            "limitations": [
                "Convenience sample of China-centric jobs",
                "Broad regex families require context reading before interpretation",
                "A mention can occur in duties, requirements, preferences, or team descriptions",
                "Job coverage is insensitive to repeated and bilingual mentions",
            ],
        },
        "corpus": {
            "path": str(args.jd_file),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "characters": len(text),
            "jobs": len(jobs),
            "core_jobs": len(core_ids),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "terms": {},
    }
    for key, spec in TERMS.items():
        all_ids = [job_id for job_id, job in jobs.items() if re.search(spec["pattern"], job["text"])]
        core_matches = sorted(set(all_ids) & set(core_ids))
        result["terms"][key] = {
            "label": spec["label"],
            "basis": spec["basis"],
            "pattern": spec["pattern"],
            "all_count": len(all_ids),
            "all_ids": all_ids,
            "core_count": len(core_matches),
            "core_ids": core_matches,
        }
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
