import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import config
from app.routes.ai_proposal_assistant import router as ai_proposal_assistant_router
from app.routes.calculate_compatibility import router as calculate_compatibility_router
from app.routes.calculate_personalized_compatibility import router as calculate_personalized_compatibility_router
from app.routes.calculate_sbert_compatibility import router as calculate_sbert_compatibility_router
from app.routes.create_search_function import router as create_search_function_router
from app.routes.generate_concept_note import router as generate_concept_note_router
from app.routes.generate_embedding import router as generate_embedding_router
from app.routes.partner_compatibility import router as partner_compatibility_router
from app.routes.process_pdf import router as process_pdf_router
from app.routes.recalculate_user_compatibility import router as recalc_user_compat_router
from app.routes.simple_chatbot import router as simple_chatbot_router

app = FastAPI(title="InsightMatches Python API")

# CORS
if config.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

@app.get("/health")
async def health():
    return {"status": "ok", "service": "insightmatches-pyapi"}

# Register routes
app.include_router(ai_proposal_assistant_router, prefix="/api/ai-proposal-assistant")
app.include_router(calculate_compatibility_router, prefix="/api/calculate-compatibility")
app.include_router(calculate_personalized_compatibility_router, prefix="/api/calculate-personalized-compatibility")
app.include_router(calculate_sbert_compatibility_router, prefix="/api/calculate-sbert-compatibility")
app.include_router(create_search_function_router, prefix="/api/create-search-function")
app.include_router(generate_concept_note_router, prefix="/api/generate-concept-note")
app.include_router(generate_embedding_router, prefix="/api/generate-embedding")
app.include_router(partner_compatibility_router, prefix="/api/partner-compatibility")
app.include_router(process_pdf_router, prefix="/api/process-pdf")
app.include_router(recalc_user_compat_router, prefix="/api/recalculate-user-compatibility")
app.include_router(simple_chatbot_router, prefix="/api/simple-chatbot")
