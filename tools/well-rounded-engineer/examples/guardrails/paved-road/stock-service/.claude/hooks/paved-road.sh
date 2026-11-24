#!/bin/bash
# PreToolUse hook for Edit|Write: deployment files come from the platform's templates.
# The agent may change service.yaml (the values); it may not write its own Dockerfile,
# Kubernetes manifests or deploy workflow, nor the hook settings. Exit 2 blocks the edit and tells the agent why.
# It catches honest mistakes; it is not a security boundary (a shell command can still write a file).
path=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')
case "$path" in
  Dockerfile|*/Dockerfile|Dockerfile.*|*/Dockerfile.*|k8s/*|*/k8s/*|helm/*|*/helm/*|.github/workflows/*|*/.github/workflows/*|.claude/*|*/.claude/*)
    echo "Blocked: $path is generated from the platform templates (or guards them). Change service.yaml instead, or ask the platform team to change the template." >&2
    exit 2 ;;
esac
exit 0
