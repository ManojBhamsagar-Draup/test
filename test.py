{
	"type" : [ "object", "null" ],
	"properties" : {
		"ticker" : {
			"type" : [ "string" ]
		},
		"company_name" : {
			"type" : [ "string" ]
		},
		"yahoo_financial_link" : {
			"type" : [ "string" ]
		},
		"data" : {
			"type" : [ "object" ],
			"properties" : {
				"financialsTemplate" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"code" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"cashflowStatementHistory" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"cashflowStatements" : {
							"type" : [ "array", "null" ],
							"items" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"investments" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeToLiabilities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCashflowsFromInvestingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netBorrowings" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCashFromFinancingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeToOperatingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"issuanceOfStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netIncome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeInCash" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"endDate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"repurchaseOfStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"effectOfExchangeRate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCashFromOperatingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"depreciation" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCashflowsFromInvestingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeToAccountReceivables" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"maxAge" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"changeToNetincome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"capitalExpenditures" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCashflowsFromFinancingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"balanceSheetHistoryQuarterly" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"balanceSheetStatements" : {
							"type" : [ "array", "null" ],
							"items" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"intangibleAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"capitalSurplus" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalStockholderEquity" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCurrentLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"endDate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"commonStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCurrentAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"retainedEarnings" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"goodWill" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"treasuryStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"cash" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCurrentLiabilities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"deferredLongTermAssetCharges" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherStockholderEquity" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"propertyPlantEquipment" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCurrentAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netTangibleAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netReceivables" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"maxAge" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"longTermDebt" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"accountsPayable" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"deferredLongTermLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"longTermInvestments" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"shortTermInvestments" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"earnings" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"earningsChart" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"quarterly" : {
									"type" : [ "array", "null" ],
									"items" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"date" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"actual" : {
												"type" : [ "object", "null" ],
												"properties" : {
													"raw" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"fmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													}
												},
												"required" : [ ]
											},
											"estimate" : {
												"type" : [ "object", "null" ],
												"properties" : {
													"raw" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"fmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													}
												},
												"required" : [ ]
											}
										},
										"required" : [ ]
									}
								},
								"currentQuarterEstimate" : {
									"type" : [ "object", "null" ],
									"properties" : {
										"raw" : {
											"type" : [ "Int", "string", "float", "null" ]
										},
										"fmt" : {
											"type" : [ "Int", "string", "float", "null" ]
										}
									},
									"required" : [ ]
								},
								"currentQuarterEstimateDate" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"currentQuarterEstimateYear" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"earningsDate" : {
									"type" : [ "array", "null" ],
									"items" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								}
							},
							"required" : [ ]
						},
						"financialsChart" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"yearly" : {
									"type" : [ "array", "null" ],
									"items" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"date" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"revenue" : {
												"type" : [ "object", "null" ],
												"properties" : {
													"raw" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"fmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"longFmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													}
												},
												"required" : [ ]
											},
											"earnings" : {
												"type" : [ "object", "null" ],
												"properties" : {
													"raw" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"fmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"longFmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													}
												},
												"required" : [ ]
											}
										},
										"required" : [ ]
									}
								},
								"quarterly" : {
									"type" : [ "array", "null" ],
									"items" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"date" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"revenue" : {
												"type" : [ "object", "null" ],
												"properties" : {
													"raw" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"fmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"longFmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													}
												},
												"required" : [ ]
											},
											"earnings" : {
												"type" : [ "object", "null" ],
												"properties" : {
													"raw" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"fmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													},
													"longFmt" : {
														"type" : [ "Int", "string", "float", "null" ]
													}
												},
												"required" : [ ]
											}
										},
										"required" : [ ]
									}
								}
							},
							"required" : [ ]
						},
						"financialCurrency" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"price" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"quoteSourceName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"regularMarketOpen" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"averageDailyVolume3Month" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"exchange" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"regularMarketTime" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"volume24Hr" : {
							"type" : [ "object", "null" ]
						},
						"regularMarketDayHigh" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"shortName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"averageDailyVolume10Day" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"longName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"regularMarketChange" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"currencySymbol" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"regularMarketPreviousClose" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"postMarketTime" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"preMarketPrice" : {
							"type" : [ "object", "null" ]
						},
						"exchangeDataDelayedBy" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"postMarketChange" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"postMarketPrice" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"exchangeName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"preMarketChange" : {
							"type" : [ "object", "null" ]
						},
						"circulatingSupply" : {
							"type" : [ "object", "null" ]
						},
						"regularMarketDayLow" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"priceHint" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"currency" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"regularMarketPrice" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"regularMarketVolume" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"regularMarketSource" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"openInterest" : {
							"type" : [ "object", "null" ]
						},
						"marketState" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"marketCap" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"quoteType" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"volumeAllCurrencies" : {
							"type" : [ "object", "null" ]
						},
						"postMarketSource" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"strikePrice" : {
							"type" : [ "object", "null" ]
						},
						"symbol" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"postMarketChangePercent" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"preMarketSource" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"regularMarketChangePercent" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						}
					},
					"required" : [ ]
				},
				"incomeStatementHistoryQuarterly" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"incomeStatementHistory" : {
							"type" : [ "array", "null" ],
							"items" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"researchDevelopment" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"effectOfAccountingCharges" : {
										"type" : [ "object", "null" ]
									},
									"incomeBeforeTax" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"minorityInterest" : {
										"type" : [ "object", "null" ]
									},
									"netIncome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"sellingGeneralAdministrative" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"grossProfit" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"ebit" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"endDate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"operatingIncome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherOperatingExpenses" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"interestExpense" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										}
									},
									"extraordinaryItems" : {
										"type" : [ "object", "null" ]
									},
									"nonRecurring" : {
										"type" : [ "object", "null" ]
									},
									"otherItems" : {
										"type" : [ "object", "null" ]
									},
									"incomeTaxExpense" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalRevenue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalOperatingExpenses" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"costOfRevenue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalOtherIncomeExpenseNet" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"maxAge" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"discontinuedOperations" : {
										"type" : [ "object", "null" ]
									},
									"netIncomeFromContinuingOps" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netIncomeApplicableToCommonShares" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"incomeStatementHistory" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"incomeStatementHistory" : {
							"type" : [ "array", "null" ],
							"items" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"researchDevelopment" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"effectOfAccountingCharges" : {
										"type" : [ "object", "null" ]
									},
									"incomeBeforeTax" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"minorityInterest" : {
										"type" : [ "object", "null" ]
									},
									"netIncome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"sellingGeneralAdministrative" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"grossProfit" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"ebit" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"endDate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"operatingIncome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherOperatingExpenses" : {
										"type" : [ "object", "null" ]
									},
									"interestExpense" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"extraordinaryItems" : {
										"type" : [ "object", "null" ]
									},
									"nonRecurring" : {
										"type" : [ "object", "null" ]
									},
									"otherItems" : {
										"type" : [ "object", "null" ]
									},
									"incomeTaxExpense" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalRevenue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalOperatingExpenses" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"costOfRevenue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalOtherIncomeExpenseNet" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"maxAge" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"discontinuedOperations" : {
										"type" : [ "object", "null" ]
									},
									"netIncomeFromContinuingOps" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netIncomeApplicableToCommonShares" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"balanceSheetHistory" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"balanceSheetStatements" : {
							"type" : [ "array", "null" ],
							"items" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"intangibleAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"capitalSurplus" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalStockholderEquity" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"deferredLongTermLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCurrentLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"endDate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"commonStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCurrentAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"retainedEarnings" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherLiab" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"goodWill" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"treasuryStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"cash" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCurrentLiabilities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"deferredLongTermAssetCharges" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherStockholderEquity" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"propertyPlantEquipment" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCurrentAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"longTermInvestments" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netTangibleAssets" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"shortTermInvestments" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netReceivables" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"maxAge" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"longTermDebt" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"accountsPayable" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"cashflowStatementHistoryQuarterly" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"cashflowStatements" : {
							"type" : [ "array", "null" ],
							"items" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"investments" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeToLiabilities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCashflowsFromInvestingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netBorrowings" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCashFromFinancingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeToOperatingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"netIncome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeInCash" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"endDate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"repurchaseOfStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"effectOfExchangeRate" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"totalCashFromOperatingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"depreciation" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCashflowsFromInvestingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"changeToAccountReceivables" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"maxAge" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"changeToNetincome" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"capitalExpenditures" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"issuanceOfStock" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									},
									"otherCashflowsFromFinancingActivities" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"longFmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"quoteType" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"exchange" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"shortName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"longName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"exchangeTimezoneName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"exchangeTimezoneShortName" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"isEsgPopulated" : {
							"type" : [ "boolean", "null" ]
						},
						"gmtOffSetMilliseconds" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"quoteType" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"symbol" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"messageBoardId" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"market" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"summaryDetail" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"previousClose" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"regularMarketOpen" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"twoHundredDayAverage" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"trailingAnnualDividendYield" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"payoutRatio" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"volume24Hr" : {
							"type" : [ "object", "null" ]
						},
						"regularMarketDayHigh" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"navPrice" : {
							"type" : [ "object", "null" ]
						},
						"averageDailyVolume10Day" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"totalAssets" : {
							"type" : [ "object", "null" ]
						},
						"regularMarketPreviousClose" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"fiftyDayAverage" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"trailingAnnualDividendRate" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"open" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"averageVolume10days" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"expireDate" : {
							"type" : [ "object", "null" ]
						},
						"yield" : {
							"type" : [ "object", "null" ]
						},
						"dividendRate" : {
							"type" : [ "object", "null" ]
						},
						"exDividendDate" : {
							"type" : [ "object", "null" ]
						},
						"beta" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"circulatingSupply" : {
							"type" : [ "object", "null" ]
						},
						"startDate" : {
							"type" : [ "object", "null" ]
						},
						"regularMarketDayLow" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"priceHint" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"currency" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"trailingPE" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"regularMarketVolume" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"maxSupply" : {
							"type" : [ "object", "null" ]
						},
						"openInterest" : {
							"type" : [ "object", "null" ]
						},
						"marketCap" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"volumeAllCurrencies" : {
							"type" : [ "object", "null" ]
						},
						"strikePrice" : {
							"type" : [ "object", "null" ]
						},
						"averageVolume" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"priceToSalesTrailing12Months" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"dayLow" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"ask" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"ytdReturn" : {
							"type" : [ "object", "null" ]
						},
						"askSize" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"volume" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"fiftyTwoWeekHigh" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"forwardPE" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"fiveYearAvgDividendYield" : {
							"type" : [ "object", "null" ]
						},
						"fiftyTwoWeekLow" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"bid" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"tradeable" : {
							"type" : [ "boolean", "null" ]
						},
						"dividendYield" : {
							"type" : [ "object", "null" ]
						},
						"bidSize" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"longFmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						},
						"dayHigh" : {
							"type" : [ "object", "null" ],
							"properties" : {
								"raw" : {
									"type" : [ "Int", "string", "float", "null" ]
								},
								"fmt" : {
									"type" : [ "Int", "string", "float", "null" ]
								}
							},
							"required" : [ ]
						}
					},
					"required" : [ ]
				},
				"symbol" : {
					"type" : [ "Int", "string", "float", "null" ]
				},
				"pageViews" : {
					"type" : [ "object", "null" ],
					"properties" : {
						"shortTermTrend" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"midTermTrend" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"longTermTrend" : {
							"type" : [ "Int", "string", "float", "null" ]
						},
						"maxAge" : {
							"type" : [ "Int", "string", "float", "null" ]
						}
					},
					"required" : [ ]
				},
				"trailingNetIncomeFromContinuingAndDiscontinuedOperation" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingPretaxIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualInterestExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualDilutedNIAvailtoComStockholders" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualSpecialIncomeCharges" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingInterestExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualInterestIncomeNonOperating" : {
					"type" : [ "array", "null" ],
					"items" : {
						"anyOf" : [
							{
								"type" : "null"
							},
							{
								"type" : [ "object", "null" ],
								"properties" : {
									"dataId" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"asOfDate" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"periodType" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"currencyCode" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"reportedValue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						]
					}
				},
				"annualPretaxIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTotalUnusualItems" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNormalizedEBITDA" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingDilutedNIAvailtoComStockholders" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualSellingGeneralAndAdministration" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOtherNonOperatingIncomeExpenses" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOtherOperatingExpenses" : {
					"type" : [ "array", "null" ]
				},
				"annualImpairmentOfCapitalAssets" : {
					"type" : [ "array", "null" ],
					"items" : {
						"anyOf" : [
							{
								"type" : "null"
							},
							{
								"type" : [ "object", "null" ],
								"properties" : {
									"dataId" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"asOfDate" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"periodType" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"currencyCode" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"reportedValue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						]
					}
				},
				"annualNetIncomeFromContinuingAndDiscontinuedOperation" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingDepreciationAndAmortizationInIncomeStatement" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualDepreciationAmortizationDepletionIncomeStatement" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingGeneralAndAdministrativeExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingEBIT" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingOperatingExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualBasicAverageShares" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualTotalExpenses" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualInterestIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"anyOf" : [
							{
								"type" : "null"
							},
							{
								"type" : [ "object", "null" ],
								"properties" : {
									"dataId" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"asOfDate" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"periodType" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"currencyCode" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"reportedValue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						]
					}
				},
				"trailingRestructuringAndMergernAcquisition" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetNonOperatingInterestIncomeExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualReconciledCostOfRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetNonOperatingInterestIncomeExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetIncomeCommonStockholders" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTotalOperatingIncomeAsReported" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTaxEffectOfUnusualItems" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetInterestIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetIncomeFromContinuingOperationNetMinorityInterest" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualTaxRateForCalcs" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetIncomeCommonStockholders" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetIncomeFromContinuingOperationNetMinorityInterest" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualReconciledDepreciation" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualBasicEPS" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualGeneralAndAdministrativeExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTaxRateForCalcs" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingAmortization" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingSpecialIncomeCharges" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingReconciledDepreciation" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingGrossProfit" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingEBITDA" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingDepreciationAmortizationDepletionIncomeStatement" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNormalizedEBITDA" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualTotalRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingOperatingRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetIncomeIncludingNoncontrollingInterests" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingOtherNonOperatingIncomeExpenses" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingInterestExpenseNonOperating" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingResearchAndDevelopment" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingOperatingIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualCostOfRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingCostOfRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTotalRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingOtherIncomeExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetIncomeFromTaxLossCarryforward" : {
					"type" : [ "array", "null" ]
				},
				"annualTaxProvision" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTaxProvision" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingAmortizationOfIntangiblesIncomeStatement" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualGrossProfit" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetIncomeIncludingNoncontrollingInterests" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingSellingAndMarketingExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualAmortization" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOperatingIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOtherIncomeExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOtherSpecialCharges" : {
					"type" : [ "array", "null" ]
				},
				"annualOperatingRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualResearchAndDevelopment" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualInterestExpenseNonOperating" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualTotalUnusualItemsExcludingGoodwill" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNormalizedIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTotalExpenses" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetIncomeContinuousOperations" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOtherGandA" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetIncomeContinuousOperations" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualTotalOperatingIncomeAsReported" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNetInterestIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualSellingAndMarketingExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingOtherGandA" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualDepreciationAndAmortizationInIncomeStatement" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualGainOnSaleOfSecurity" : {
					"type" : [ "array", "null" ],
					"items" : {
						"anyOf" : [
							{
								"type" : "null"
							},
							{
								"type" : [ "object", "null" ],
								"properties" : {
									"dataId" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"asOfDate" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"periodType" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"currencyCode" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"reportedValue" : {
										"type" : [ "object", "null" ],
										"properties" : {
											"raw" : {
												"type" : [ "Int", "string", "float", "null" ]
											},
											"fmt" : {
												"type" : [ "Int", "string", "float", "null" ]
											}
										},
										"required" : [ ]
									}
								},
								"required" : [ ]
							}
						]
					}
				},
				"annualTaxEffectOfUnusualItems" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingReconciledCostOfRevenue" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualAmortizationOfIntangiblesIncomeStatement" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualDilutedEPS" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualTotalUnusualItems" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNormalizedIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualDilutedAverageShares" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualEBIT" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualNetIncome" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualRestructuringAndMergernAcquisition" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingTotalUnusualItemsExcludingGoodwill" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"annualOperatingExpense" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingSellingGeneralAndAdministration" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "object", "null" ],
						"properties" : {
							"dataId" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"asOfDate" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"periodType" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"currencyCode" : {
								"type" : [ "Int", "string", "float", "null" ]
							},
							"reportedValue" : {
								"type" : [ "object", "null" ],
								"properties" : {
									"raw" : {
										"type" : [ "Int", "string", "float", "null" ]
									},
									"fmt" : {
										"type" : [ "Int", "string", "float", "null" ]
									}
								},
								"required" : [ ]
							}
						},
						"required" : [ ]
					}
				},
				"trailingNormalizedBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedDiscontinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedAverageShares" : {
					"type" : [ "array", "null" ]
				},
				"annualRentAndLandingFees" : {
					"type" : [ "array", "null" ]
				},
				"annualWriteOff" : {
					"type" : [ "array", "null" ]
				},
				"trailingGainOnSaleOfSecurity" : {
					"type" : [ "array", "null" ]
				},
				"annualGainOnSaleOfPPE" : {
					"type" : [ "array", "null" ]
				},
				"trailingReportedNormalizedBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualEarningsFromEquityInterest" : {
					"type" : [ "array", "null" ]
				},
				"trailingOtherunderPreferredStockDividend" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicAccountingChange" : {
					"type" : [ "array", "null" ]
				},
				"trailingContinuingAndDiscontinuedDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualDilutedContinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedAccountingChange" : {
					"type" : [ "array", "null" ]
				},
				"annualBasicAccountingChange" : {
					"type" : [ "array", "null" ]
				},
				"annualNetIncomeExtraordinary" : {
					"type" : [ "array", "null" ]
				},
				"trailingOtherTaxes" : {
					"type" : [ "array", "null" ]
				},
				"trailingInterestIncome" : {
					"type" : [ "array", "null" ]
				},
				"annualAverageDilutionEarnings" : {
					"type" : [ "array", "null" ]
				},
				"annualSalariesAndWages" : {
					"type" : [ "array", "null" ]
				},
				"annualContinuingAndDiscontinuedBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingNetIncomeDiscontinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"trailingDepreciationIncomeStatement" : {
					"type" : [ "array", "null" ]
				},
				"trailingOtherOperatingExpenses" : {
					"type" : [ "array", "null" ]
				},
				"annualExciseTaxes" : {
					"type" : [ "array", "null" ]
				},
				"trailingEarningsFromEquityInterest" : {
					"type" : [ "array", "null" ]
				},
				"annualDilutedEPSOtherGainsLosses" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicExtraordinary" : {
					"type" : [ "array", "null" ]
				},
				"annualTotalOtherFinanceCost" : {
					"type" : [ "array", "null" ]
				},
				"trailingAverageDilutionEarnings" : {
					"type" : [ "array", "null" ]
				},
				"annualSecuritiesAmortization" : {
					"type" : [ "array", "null" ]
				},
				"trailingContinuingAndDiscontinuedBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedEPSOtherGainsLosses" : {
					"type" : [ "array", "null" ]
				},
				"trailingEarningsFromEquityInterestNetOfTax" : {
					"type" : [ "array", "null" ]
				},
				"trailingExciseTaxes" : {
					"type" : [ "array", "null" ]
				},
				"annualPreferredStockDividends" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedExtraordinary" : {
					"type" : [ "array", "null" ]
				},
				"annualReportedNormalizedDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualRentExpenseSupplemental" : {
					"type" : [ "array", "null" ]
				},
				"annualDepletionIncomeStatement" : {
					"type" : [ "array", "null" ]
				},
				"annualReportedNormalizedBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualBasicDiscontinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"annualDilutedDiscontinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"trailingMinorityInterests" : {
					"type" : [ "array", "null" ]
				},
				"annualDepreciationIncomeStatement" : {
					"type" : [ "array", "null" ]
				},
				"annualBasicContinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"annualNormalizedDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualGainOnSaleOfBusiness" : {
					"type" : [ "array", "null" ]
				},
				"trailingNetIncomeExtraordinary" : {
					"type" : [ "array", "null" ]
				},
				"trailingInsuranceAndClaims" : {
					"type" : [ "array", "null" ]
				},
				"trailingRentAndLandingFees" : {
					"type" : [ "array", "null" ]
				},
				"trailingSalariesAndWages" : {
					"type" : [ "array", "null" ]
				},
				"annualContinuingAndDiscontinuedDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualDilutedExtraordinary" : {
					"type" : [ "array", "null" ]
				},
				"trailingWriteOff" : {
					"type" : [ "array", "null" ]
				},
				"annualNetIncomeDiscontinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"annualInsuranceAndClaims" : {
					"type" : [ "array", "null" ]
				},
				"annualProvisionForDoubtfulAccounts" : {
					"type" : [ "array", "null" ]
				},
				"trailingOtherSpecialCharges" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicContinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"trailingInterestIncomeNonOperating" : {
					"type" : [ "array", "null" ]
				},
				"trailingTaxLossCarryforwardDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingDividendPerShare" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicEPSOtherGainsLosses" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingNormalizedDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualBasicEPSOtherGainsLosses" : {
					"type" : [ "array", "null" ]
				},
				"trailingNetIncomeFromTaxLossCarryforward" : {
					"type" : [ "array", "null" ]
				},
				"trailingProvisionForDoubtfulAccounts" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicAverageShares" : {
					"type" : [ "array", "null" ]
				},
				"annualTaxLossCarryforwardDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingImpairmentOfCapitalAssets" : {
					"type" : [ "array", "null" ]
				},
				"trailingDepletionIncomeStatement" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualTaxLossCarryforwardBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualOtherTaxes" : {
					"type" : [ "array", "null" ]
				},
				"trailingDilutedContinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"annualDilutedAccountingChange" : {
					"type" : [ "array", "null" ]
				},
				"annualDividendPerShare" : {
					"type" : [ "array", "null" ]
				},
				"annualEarningsFromEquityInterestNetOfTax" : {
					"type" : [ "array", "null" ]
				},
				"trailingReportedNormalizedDilutedEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualBasicExtraordinary" : {
					"type" : [ "array", "null" ]
				},
				"annualMinorityInterests" : {
					"type" : [ "array", "null" ]
				},
				"annualOtherunderPreferredStockDividend" : {
					"type" : [ "array", "null" ]
				},
				"trailingPreferredStockDividends" : {
					"type" : [ "array", "null" ]
				},
				"trailingSecuritiesAmortization" : {
					"type" : [ "array", "null" ]
				},
				"trailingTotalOtherFinanceCost" : {
					"type" : [ "array", "null" ]
				},
				"trailingBasicDiscontinuousOperations" : {
					"type" : [ "array", "null" ]
				},
				"trailingTaxLossCarryforwardBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"annualNormalizedBasicEPS" : {
					"type" : [ "array", "null" ]
				},
				"trailingGainOnSaleOfPPE" : {
					"type" : [ "array", "null" ]
				},
				"trailingGainOnSaleOfBusiness" : {
					"type" : [ "array", "null" ]
				},
				"trailingRentExpenseSupplemental" : {
					"type" : [ "array", "null" ]
				},
				"timestamp" : {
					"type" : [ "array", "null" ],
					"items" : {
						"type" : [ "Int", "string", "float", "null" ]
					}
				}
			},
			"required" : [ ]
		},
		"company_price_details" : {
			"type" : [ "string", "null" ]
		},
		"company_currency_details" : {
			"type" : [ "string", "null" ]
		},
		"quote_market_notice" : {
			"type" : [ "string", "null" ]
		}
	},
	"required" : [ ]
}