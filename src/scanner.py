from dataclasses import dataclass

@dataclass(frozen=True)
class ResourceFinding:
    resource_id: str
    resource_type: str
    reason: str
    confidence: float
    monthly_savings: float

def rank_findings(findings: list[ResourceFinding]) -> list[ResourceFinding]:
    return sorted(findings, key=lambda x: (x.confidence, x.monthly_savings), reverse=True)

def is_low_utilization(avg_cpu: float, threshold: float = 5.0) -> bool:
    if not 0 <= avg_cpu <= 100:
        raise ValueError("avg_cpu must be between 0 and 100")
    return avg_cpu < threshold
